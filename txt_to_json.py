import os
import argparse
import json

class Item():
    def __init__(self):
        self.id = None
        self.case = None
        self.question = None
        self.options = None


def main():
    # code goes here
    parser = argparse.ArgumentParser(description='Given a text file, put it into a JSON document where each item has a Case, Question, and Options')
    parser.add_argument('--input', type = str, default='sample_input.txt', help='the name of the input text file')
    parser.add_argument('--output', type = str, default='sample_output.json', help='the name of the output json file')

    args = parser.parse_args()
    input_fname = args.input
    output_fname = args.output
    
    with open(input_fname, 'r') as f:
        lines = f.readlines() # array of strings where each element is a line
        for line in lines:
            print(line)


if __name__ == '__main__':
    main()
