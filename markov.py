from histograms import Dictogram
import random
from collections import deque
import re


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
    # To just generate any starting word uncomment line:
    # return random.choice(model.keys())

    # To generate a "valid" starting word use:
    # Valid starting words are words that started a sentence in the corpus
    if 'END' in model:
        seed_word = 'END'
        while seed_word == 'END':
            seed_word = model['END'].return_weighted_random_word()
        return seed_word
    return random.choice(model.keys())


def generate_random_sentence(length, markov_model):
    current_word = generate_random_start(markov_model)
    sentence = [current_word]
    for i in range(0, length):
        current_dictogram = markov_model[current_word]
        random_weighted_word = current_dictogram.return_weighted_random_word()
        current_word = random_weighted_word
        sentence.append(current_word)
    sentence[0] = sentence[0].capitalize()
    return ' '.join(sentence) + '.'
    return sentence


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
    # Length denotes the max amount of chars

    current_window = generate_random_start(markov_model)
    sentence = [current_window[0]]
    tweet = ''

    valid_tweet_flag = True
    sentence_count = 0
    while valid_tweet_flag:
        # We will generate random sentences until we decide we can not any more
        current_dictogram = markov_model[current_window]
        random_weighted_word = current_dictogram.return_weighted_random_word()

        current_window_deque = deque(current_window)
        current_window_deque.popleft()
        current_window_deque.append(random_weighted_word)
        current_window = tuple(current_window_deque)
        sentence.append(current_window[0])
        if sentence[len(sentence)-1] == 'END':
            sentence_string = ' '.join(sentence)
            sentence_string = re.sub(' END', '. ', sentence_string, flags=re.IGNORECASE)
            sentence_string = sentence_string.capitalize()

            new_tweet_len = len(sentence_string) + len(tweet)

            if sentence_count == 0 and new_tweet_len < length:
                # We should add this sentence to the tweet and move on to
                # make another
                tweet += sentence_string
                sentence_count += 1
                current_window = generate_random_start(markov_model)
                sentence = [current_window[0]]
            elif sentence_count == 0 and new_tweet_len >= length:
                # forget the sentence and generate a new one :P
                current_window = generate_random_start(markov_model)
                sentence = [current_window[0]]
            elif sentence_count > 0 and new_tweet_len < length:
                # More than one sentence. and length is still less max
                # Get another new sentence
                tweet += sentence_string
                sentence_count += 1
                current_window = generate_random_start(markov_model)
                sentence = [current_window[0]]
            else:
                # Return this good good tweet
                return tweet


def get_sentence_starters(file):
    result = []
    for i in range(0, len(file)-2):
        if file[i] == 'END':
            result.append(file[i+1])
    return result


# Personal Tests - leaving until after code review incase we need to test
import cleanup
file_name = 'drSeussQuotes.txt'
cleaned_file = cleanup.clean_file(file_name)
start_words = get_sentence_starters(cleaned_file)

markov_model_nth = make_higher_order_markov_model(2, cleaned_file)
for key in markov_model_nth:
    print key, markov_model_nth[key]

print generate_random_sentence_n(140, markov_model_nth)
