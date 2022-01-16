"""
   The goal of this python script is to reverse the string(s) input that the
   user enters and print the result

   If the user enters one word then that word is reversed
   Example:
     python stringReversal.py Hello
     'olleH'

   If the user enters more than one word than the order the words are inputed
   are reversed.
   Example:
     python stringReversal.py Hello World
     'World Hello'
"""

import sys


def reverse_word(word):
    '''This function
    :return the orignal word reversed
    '''
    reversed_word = ""
    for i in range(0, len(word)):
        reversed_word += word[len(word) - 1 - i]
    return reversed_word


def reverse_list(sentence):
    reversed_sentence = ""
    for i in range(0, len(sentence)):
        reversed_sentence += sentence[len(sentence) - 1 - i] + ' '
    return reversed_sentence


argument_list = list(sys.argv)
# Remove the command input from argv list
argument_list.pop(0)

if len(argument_list) == 1:
    print(reverse_word(argument_list[0]))
else:
    print(reverse_list(argument_list))
    # for i in argument_lis:
