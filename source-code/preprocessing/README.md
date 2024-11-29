# Preprocessing

This directory contains some examples of data preprocessing.


## What is it?

1. `environment.yml`: conda environment file for installing the necessary
   dependencies.
1. `preprocess_openmp_faq.py`: Python script that reads the OpenMP FAQ from an
   HTML file, and writes the output to standard output.  The output is in JSONL
   format, with each question-answer pair on a single line.
1. `openmp_faq.html`: HTML file containing the OpenMP FAQ.
1. `openmp_faq.jsonl`: JSONL file containing the OpenMP FAQ in a structured
   format.
1. `preprocess_pandas_faq.py`: Python script that reads the pandas data
   analysis FAQ from a "CSV" file, and writes the output to standard output.
   The output is in JSONL format, with each question-answer pair on a single
   line.
1. `pandas_data_analysis_questions.csv`: "CSV" file containing the pandas data
   analysis FAQ. (Source: Hugging Face DinaZahran/pandas_data_analysis_questions
   dataset.)
1. `pandas_data_analysis_questions.jsonl`: JSONL file containing the pandas
   data analysis FAQ in a structured format.
1. `split_jsonl.py`: Python script that reads a JSONL file, and splits into
   two files, one containing the training data, the other the test data.
