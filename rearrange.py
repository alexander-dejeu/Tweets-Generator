"""
   The intention of this script is to take user inputs and then shuffle
   up the order the inputs and print the shuffled user inputs

   For Example:
   python rearrange.py Hello My Name Is Alex

   Will print any random arangement of Hello, My, Name, Is, and Alex
   Possible to print in the same order as inputed.
"""
import sys
import random

print('Number of arguments:', len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv))

original_arg_list = sys.argv
random_order_list = []

# Start the range a index 1 not 0 because the first argv is the command input
# and not relevant to the user inputs
for i in range(1, len(sys.argv)):
    random_num = random.randint(1, len(original_arg_list)-1)
    random_order_list.append(original_arg_list[random_num])
    original_arg_list.remove(original_arg_list[random_num])

print(random_order_list)
