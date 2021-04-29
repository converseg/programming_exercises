import argparse
import json

class Item():
    # input: an array of strings. These get parsed into a Case, Question, and Options
    def __init__(self, text):
        self.entry = {}
        self.case = None
        self.question = None
        self.options = None
        # TODO: what if the input file is not formatted exactly the same?
        case = text[0]
        question = text[1]
        options = text[2:] # what if no options are given and the index is out of bounds?
        try: 
            # make sure that format of the input file matches our expectation
            assert(case[:5] == 'Case:')
            assert(question[:9] == 'Question:')
            for option in options:
                assert(option[0] == '-')
            # try to format nicely:
            #   remove the 'Case: ', 'Question: ', and '- ' headers
            #   remove each line break at the end of each string
            self.case = case[6:-1]
            self.question = question[10:-1]
            self.options = []
            for option in options:
                self.options.append(option[2:-1])
        except:
            print('Unusual input item')
            # when given an input file with different format, we should flag and handle it differently
            # for now, just write an empty "item" to the json file
        
        self.entry['case'] = self.case
        self.entry['question'] = self.question
        self.entry['options'] = self.options


def main():
    parser = argparse.ArgumentParser(description='Given a text file, put it into a JSON document where each item has a Case, Question, and Options')
    parser.add_argument('--input', type = str, default='sample_input.txt', help='the name of the input text file')
    parser.add_argument('--output', type = str, default='sample_output.json', help='the name of the output json file')

    args = parser.parse_args()
    input_fname = args.input
    output_fname = args.output

    start_index = 0
    all_items = [] # a list of Item objects
    with open(input_fname, 'r') as f:
        lines = f.readlines() 
        for i, line in enumerate(lines):
            if line == '###\n': # this string signals that the last item ended, and we can start making a new item
                item_text = lines[start_index: i]
                all_items.append(Item(item_text))
                start_index = i+1 # the next item will start with the line after ###

    json_data = {}
    json_data['items'] = []
    for item in all_items:
        json_data['items'].append(item.entry)
    with open(output_fname, 'w') as f:
        json.dump(json_data, f, indent=2) 

if __name__ == '__main__':
    main()
