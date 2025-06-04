#!/usr/bin/env python

import argparse
import arxiv
import crewai
import crewai_tools
import datetime
import os
import pydantic
import time
import typing


# set parameters to use
RATE_LIMIT_DELAY = 5

class FetchArxivPapersInput(pydantic.BaseModel):
    '''Input schema for FetchArxivPapersTool.
    '''
    target_date: datetime.date = pydantic.Field(..., description='Target date to fetch papers for.')


class FetchArxivPapersTool(crewai.tools.BaseTool):
    '''Tool to fetch ArXiv papers from selected categories submitted on a specific date.
    '''
    name: str = 'fetch_arxiv_papers'
    description: str = 'Fetches all ArXiv papers from selected categories submitted on the target date.'
    args_schema: typing.Type[pydantic.BaseModel] = FetchArxivPapersInput

    def _run(self, target_date: datetime.date) -> list[dict]:
        # List of AI-related categories. 
        AI_CATEGORIES = ['cs.CL', 'cs.AI', 'cs.LG', 'cs.CV', 'cs.NE', 'cs.RO', 'stat.ML',]

        # Define the date range for the target date
        start_date = target_date.strftime('%Y%m%d%H%M')
        end_date = (target_date + datetime.timedelta(days=1)).strftime('%Y%m%d%H%M')

        # Initialize the ArXiv client
        client = arxiv.Client(
            page_size=100,  # Fetch 100 results per page
            delay_seconds=RATE_LIMIT_DELAY,  # Respect rate limits
        )

        all_papers = []

        for category in AI_CATEGORIES:
            print(f'Fetching papers for category: {category}')

            search_query = f'cat:{category} AND submittedDate:[{start_date} TO {end_date}]'

            search = arxiv.Search(
                query=search_query,
                sort_by=arxiv.SortCriterion.SubmittedDate,
                max_results=None  # Fetch all results
            )

            # Collect results for the category
            category_papers = []
            for result in client.results(search):
                category_papers.append({
                    'title': result.title,
                    'authors': [author.name for author in result.authors],
                    'summary': result.summary,
                    'published': result.published,
                    'url': result.entry_id
                })

                # Delay between requests to respect rate limits
                time.sleep(RATE_LIMIT_DELAY)

            print(f"Fetched {len(category_papers)} papers from {category}")
            all_papers.extend(category_papers)

        return all_papers


if __name__ == "__main__":
    # parse command line arguments
    parser = argparse.ArgumentParser(description='Fetch AI research papers from ArXiv and create top-10')
    parser.add_argument('--date', type=str, required=True,
                        help='Date to fetch papers for (YYYY-MM-DD)')
    parser.add_argument('--output', type=str, default='ai_research_report.html',
                        help='Output HTML file name')
    parser.add_argument('--model', type=str, default='ollama/llama3.2:latest',
                        help='ollama LLM model to use')
    parser.add_argument('--port', type=int, default=11434,
                        help='Port for the Ollama server')
    args = parser.parse_args()

    # initialize the crewai LLM with Ollama
    llm = crewai.LLM(
        model=args.model,
        base_url=f'http://localhost:{args.port}',
    )

    # create the search tool
    arxiv_search_tool = FetchArxivPapersTool()

    # create the crewai agent to fetch and rank the papers
    researcher = crewai.Agent(
        role='Senior Researcher',
        goal='Find the top 10 papers from the search results from ArXiv on {date}.'
             'Rank them appropirately.',
        backstory='You are a senior researcher with a deep understanding of all topics in AI and AI research.'
                  'You are able to identify the best research papers based on the title and abstract.',
        verbose=True,
        llm=llm,
        tools=[arxiv_search_tool],
    )

    # create the crewai agent to compile the results into a HTML file
    frontend_engineer = crewai.Agent(
        role='Senior Frontend & AI Engineer',
        goal='Compile the results into a HTML file.',
        backstory='You are a competent frontend engineer writing HTML and CSS with decades of experience.'
                   'You have also been working with AI for decades and understand it well.',
        llm=llm,
        verbose=True,
    )

    # create the research task to find the top 10 research papers from ArXiv
    research_task = crewai.Task(
        description=(f'Find the top 10 research papers from the search results from ArXiv on {args.date}.'),
        expected_output=(
            'A list of top 10 research papers with the following information in the following format:'
            '- Title'
            '- Authors'
            '- Abstract'
            '- Link to the paper'
        ),
        agent=researcher,
        human_input=True,
    )

    # create the reporting task to compile the results into a HTML file
    reporting_task = crewai.Task(
        description=('Compile the results into a detailed report in a HTML file.'),
        expected_output=(
            'An HTML file with the results in the following format:'
            'Top 10 AI Research Papers published on {date}'
            '- Title (which on clicking opens the paper in a new tab)'
            '- Authors'
            '- Short summary of the abstract (2-4 sentences)'
        ),
        agent=frontend_engineer,
        context=[research_task],
        output_file='./ai_research_report.html',
        human_input=True,
    )


    # create the crew of agents to execute the tasks
    arxiv_research_crew = crewai.Crew(
        agents=[researcher, frontend_engineer],
        tasks=[research_task, reporting_task],
        verbose=True,
    )

    # kickoff the crew with the input date
    crew_inputs = {
        "date": args.date,
    }
    result = arxiv_research_crew.kickoff(inputs=crew_inputs)
