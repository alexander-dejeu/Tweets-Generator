import sys
import re


def clean_file(filename):
    data_file = open(filename, 'r')
    words_list = data_file.read().lower()
    result_list = []

    matches = re.findall("[A-z]+\'?[A-z]*|\$[0-9]*", words_list)
    for match in matches:
        result_list.append(match)
    return result_list


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

main()
