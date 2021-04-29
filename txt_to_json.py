import os
import argparse
import json

class Item():
    def __init__(self, text):
        self.text_array = text
        # TODO: this is hardcoded -- what if the input file is not formatted exactly the same?
        case = self.text_array[0]
        question = self.text_array[1]
        options = self.text_array[2:]
        try: # try to remove the 'Case: ', 'Question: ', and '- ' headers, along with each line break 
            assert(case[:5] == 'Case:')
            assert(question[:9] == 'Question:')
            assert(options[0][0] == '-') # i'm only checking the first option here, TODO
            self.case = case[6:-1]
            self.question = question[10:-1]
            self.options = []
            for option in options:
                self.options.append(option[2:-1])
            
        except:
            print('Unusual input file')
            self.case = case
            self.question = question
            self.options = options



def main():
    # code goes here
    parser = argparse.ArgumentParser(description='Given a text file, put it into a JSON document where each item has a Case, Question, and Options')
    parser.add_argument('--input', type = str, default='sample_input.txt', help='the name of the input text file')
    parser.add_argument('--output', type = str, default='sample_output.json', help='the name of the output json file')

    args = parser.parse_args()
    input_fname = args.input
    output_fname = args.output

    start_index = 0
    all_items = []
    with open(input_fname, 'r') as f:
        lines = f.readlines() # array of strings where each element is a line
        for i, line in enumerate(lines):
            if line == '###\n': # this string signals that the last item ended, and we can start making a new item
                item_text = lines[start_index: i]
                all_items.append(Item(item_text))
                start_index = i+1 # the next item will start with the line after ###

    for item in all_items:
        print(item.case)
        print('***')
        print(item.question)
        print('***')
        print(item.options)
        print('\n ********* NEXT ITEM ******\n')


if __name__ == '__main__':
    main()
