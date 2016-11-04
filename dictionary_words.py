"""
    The purpose of this script is to randomly print x amount of random words
    from the small_dictionary.txt file.  x is user input when calling

    Example:
      python dictionary_words.py 4
      Fox Golf Igloo Maybe
"""

import sys
import random

def get_random_int():
    return random.randint(0, len(all_words)-1)


# Open the dictionary
dictionary_file = open('small_dictionary.txt', 'r')
all_words = dictionary_file.read().splitlines()

user_argument_count = len(sys.argv)
if user_argument_count == 1:
    print 'Please enter another argument with the ammount of words to print'
else:
    amount_of_random_words = int(sys.argv[1])
    for i in range(0, amount_of_random_words):
        print all_words[get_random_int()]
# Done with the dictionary - close it
dictionary_file.close()
