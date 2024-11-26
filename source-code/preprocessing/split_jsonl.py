#!/usr/bin/env python

import argparse
import random


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input', type=str, help='Input file')
    parser.add_argument('--fraction_test', type=float, default=0.1, help='Fraction of test data')
    parser.add_argument('--train', type=str, help='File for train data')
    parser.add_argument('--test', type=str, help='File for test data')
    parser.add_argument('--seed', type=int, default=1234, help='Random seed')
    args = parser.parse_args()

    random.seed(args.seed)
    with open(args.input, 'r') as input_file, open(args.train, 'w') as train_file, open(args.test, 'w') as test_file:
        for line in input_file:
            if random.random() < args.fraction_test:
                test_file.write(line)
            else:
                train_file.write(line)

if __name__ == '__main__':
    main()
