import argparse
import json
from os import path

class Item():
    # input: an array of strings. These get parsed into a Case, Question, and Options
    def __init__(self, text):
        self.entry = {}
        self.case = None
        self.question = None
        self.options = None
        # TODO: what if the input file is not formatted exactly the same?
        case = text[0].split(' ') #array where the first element is either "Case:" or "passage:"
        case[-1] = case[-1][:-1]
        question = text[1].split(' ') #Question or Stem
        question[-1] = question[-1][:-1]
        options = text[2:] # if no options are given, then this is just an empty array []
        # try to format nicely:
        #   remove the 'Case: ', 'Question: ', and '- ' headers
        #   remove each line break at the end of each string
        self.case = ' '.join(case[1:])
        self.question = ' '.join(question[1:])
        self.options = []
        for option in options:
            if option[0] == '-':
                self.options.append(option[2:-1])
            else:
                self.options.append(option[:-1])
        
        self.entry['case'] = self.case
        self.entry['question'] = self.question
        self.entry['options'] = self.options

def write_to_json(input_fname, output_fname):
    start_index = 0
    all_items = [] # a list of Item objects
    with open(input_fname, 'r') as f:
        lines = f.readlines() 
        #long_string = f.read() # everything
        #array = long_string.split(delim="###\n") # each element is the full text of item
        for i, line in enumerate(lines):
            if line == '###\n' or line == '@@@\n': # this string signals that the last item ended, and we can start making a new item
                item_text = lines[start_index: i]
                all_items.append(Item(item_text))
                start_index = i+1 # the next item will start with the line after ###

    json_data = {}
    json_data['items'] = []
    for item in all_items:
        json_data['items'].append(item.entry)
    with open(output_fname, 'w') as f:
        json.dump(json_data, f, indent=2) 

def main():
    parser = argparse.ArgumentParser(description='Given a text file, put it into a JSON document where each item has a Case, Question, and Options')
    parser.add_argument('--input', type = str, default='sample_input.txt', help='the name of the input text file')
    parser.add_argument('--output', type = str, default='sample_output.json', help='the name of the output json file')

    args = parser.parse_args()
    input_fname = args.input
    output_fname = args.output
    if path.exists(input_fname):
        write_to_json(input_fname, output_fname)
    else:
        print('Input file not found')

if __name__ == '__main__':
    main()
