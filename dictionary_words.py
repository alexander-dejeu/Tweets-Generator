"""
    The purpose of this script is to randomly print x amount of random words
    from the small_dictionary.txt file.  x is user input when calling

    Example:
      python dictionary_words.py 4
      Fox Golf Igloo Maybe
"""

import sys
import random
from datetime import datetime


# word_list = words_file.reade().strip().split('\n')
# words_file.readlines()


def get_random_int(data_set):
    return random.randint(0, len(data_set)-1)


def generate_random_strings():
    # Open the dictionary
    dictionary_file = open('/usr/share/dict/words', 'r')
    all_words = dictionary_file.read().splitlines()

    user_argument_count = len(sys.argv)
    result_sentence = []
    if user_argument_count == 1:
        print 'Error: Amount of words to generate not provided'
    else:
        amount_of_random_words = int(sys.argv[1])
        for i in range(0, amount_of_random_words):
            random_int = get_random_int(all_words)
            result_sentence.append(all_words[random_int])


    print ' '.join(result_sentence) + '.'
    # Done with the dictionary - close it
    dictionary_file.close()


def main():
    base_start_time = datetime.now()
    generate_random_strings()
    base_end_time = datetime.now()
    base_run_time = base_end_time - base_start_time
    print base_run_time


main()
