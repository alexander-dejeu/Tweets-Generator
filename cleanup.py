import sys
import re


def clean_file(filename):
    data_file = open(filename, 'r')
    words_list = data_file.read().lower()
    words_list = remove_punctuation(words_list)
    result_list = []

    matches = re.findall("[A-z]+\'?[A-z]*|\$[0-9]*", words_list)
    for match in matches:
        result_list.append(match)
    return ['END'] + result_list

def remove_punctuation(text):
    no_punc_text = re.sub('[,()]', '', text)
    # Handles all that are not endlines
    no_punc_text = re.sub('\. +', ' END', no_punc_text)
    # This does the same as above but also gets new lines and therefore
    # we give an extra space!
    no_punc_text = re.sub('\.\s+', ' END ', no_punc_text)
    no_punc_text = re.sub('--', ' ', no_punc_text)
    no_punc_text = re.sub(':', ' ', no_punc_text)

    return no_punc_text

def main():
    user_argument_count = len(sys.argv)
    if user_argument_count == 1:
        print 'Error: textfile not provided'
    else:
        data_file = open(sys.argv[1], 'r')
        words_list = data_file.read().lower()
        # print words_list

        matches = re.findall("[A-z]+\'?[A-z]*|\$[0-9]*", words_list)
        for match in matches:
            print match
