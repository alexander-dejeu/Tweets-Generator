import sys
import re


def main():
    user_argument_count = len(sys.argv)
    if user_argument_count == 1:
        print 'Error: textfile not provided'
    else:
        data_file = open(sys.argv[1], 'r')
        words_list = data_file.read()
        print words_list

        matches = re.findall("[A-z]+\'?[A-z]*|\$[0-9]*", words_list)
        for match in matches:
            print match

main()
