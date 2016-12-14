import cleanup
from histograms import Dictogram
import random
from collections import deque
# import word_frequency

# print cleaned_file

# For every word in the cleaned file - go through and create a historgram for the value
def make_markov_model(data):
    markov_model = dict()

    for i in range(0, len(data)-1):
        if data[i] in markov_model:
            # We have to just append to the existing histogram?
            markov_model[data[i]].update([data[i+1]])
        else:
            markov_model[data[i]] = Dictogram([data[i+1]])
    return markov_model

def generate_random_start(model):
    return random.choice(model.keys())


def generate_random_sentence(length, markov_model):
    current_word = generate_random_start(markov_model)
    sentence = [current_word]
    for i in range(0, length):
        current_dictogram = markov_model[current_word]
        # print current_dictogram
        random_weighted_word = current_dictogram.return_weighted_random_word()
        current_word =  random_weighted_word
        # print 'current word: ' + current_word
        sentence.append(current_word)
    sentence[0] = sentence[0].capitalize()
    return ' '.join(sentence) + '.'
    return sentence


file_name = 'SiliconValley.txt'
cleaned_file = cleanup.clean_file(file_name)

markov_model = make_markov_model(cleaned_file)
print generate_random_sentence(15, markov_model)

## Hello Alex. Hello John how are you
## Hello, 1 --> ((Alex, 1) --> Hello),
##            (((John,1) --> how))
##           )
##
##
## ( (HEAD, (#, DICTOGRAM))
## DICTOGRAM has KEYS that are t (Hello , 1) --> None
##


def make_higher_order_markov_model(order, data):
    markov_model = dict()

    for i in range(0, len(data)-order):
        # Create the window
        window = tuple(data[i: i+order])
        # Add to the dictionary
        if window in markov_model:
            # We have to just append to the existing histogram?
            markov_model[window].update([data[i+order]])
        else:
            markov_model[window] = Dictogram([data[i+order]])

    return markov_model


def generate_random_sentence_n(length, markov_model):
    current_window = generate_random_start(markov_model)
    sentence = [current_window[0]]
    # for i in range (0, len(current_window)):
    #     sentence.append(current_window[i])

    for i in range(0, length):
        # print 'THE CURRENT WINDOW', current_window
        current_dictogram = markov_model[current_window]
        # print current_dictogram
        random_weighted_word = current_dictogram.return_weighted_random_word()
        current_window_deque = deque(current_window)
        current_window_deque.popleft()
        current_window_deque.append(random_weighted_word)

        current_window = tuple(current_window_deque)
        sentence.append(current_window[0])
    sentence = list(sentence)
    sentence[0] = sentence[0].capitalize()
    return ' '.join(sentence) + '.'
    return sentence


file_name = 'SiliconValley.txt'
cleaned_file = cleanup.clean_file(file_name)

markov_model_nth = make_higher_order_markov_model(3, cleaned_file)
# print markov_model_nth
print generate_random_sentence_n(15, markov_model_nth)
#
# markov_window = dict()
#
# for i in range(0, len(cleaned_file)-1):
#     if cleaned_file[i] in markov_model:
#         # We have to just append to the existing histogram?
#         markov_window[cleaned_file[i]].update([cleaned_file[i+1]])
#     else:
#         markov_window[cleaned_file[i]] = Dictogram([cleaned_file[i+1]])
#
# # print markov_model
#
# # Get random start word
# random_start = random.choice(markov_window.keys())
# # print random_start
# current_word = random_start
#
# sentence = [current_word]
# for i in range(0, 15):
#     current_dictogram = markov_window[current_word]
#     # print current_dictogram
#     random_weighted_word = current_dictogram.return_weighted_random_word()
#     current_word =  random_weighted_word
#     # print 'current word: ' + current_word
#     sentence.append(current_word)
#
# print sentence
#
