#!/usr/bin/env python

import argparse
from enum import Enum
import re


class State(Enum):
    NONE = 0
    Q = 1
    A = 2


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input', help='Input file')
    args = parser.parse_args()
    with open(args.input, 'r') as input_file:
        state = State.NONE
        buffer = None
        question = None
        answer = None
        for line in input_file:
            line = line.strip()
            if line.startswith('"<|user|>'):
                state = State.Q
                buffer = []
                continue
            elif line.startswith('<|assistant|>'):
                state = State.A
                buffer = []
                continue
            elif line.endswith('<|end|>'):
                line = line[:-7]
                if state == State.Q:
                    line = re.sub(r'^\d+\.\s+', '', line)
                buffer.append(line)
                if state == State.Q:
                    question = ' '.join(buffer)
                elif state == State.A:
                    answer = '\\n'.join(buffer)
                    print(f'{{"input": "{question}", "output": "{answer}"}}')
                state = State.NONE
                continue
            elif state != State.NONE:
                buffer.append(line)


if __name__ == '__main__':
    main()
