import cleanup
from histograms import Dictogram
import random
# import word_frequency

file_name = 'SiliconValley.txt'
cleaned_file = cleanup.clean_file(file_name)

# print cleaned_file

# For every word in the cleaned file - go through and create a historgram for the value
markov_model = dict()

for i in range(0, len(cleaned_file)-1):
    if cleaned_file[i] in markov_model:
        # We have to just append to the existing histogram?
        markov_model[cleaned_file[i]].update([cleaned_file[i+1]])
    else:
        markov_model[cleaned_file[i]] = Dictogram([cleaned_file[i+1]])

# print markov_model

# Get random start word
random_start = random.choice(markov_model.keys())
# print random_start
current_word = random_start

sentence = [current_word]
for i in range(0, 15):
    current_dictogram = markov_model[current_word]
    # print current_dictogram
    random_weighted_word = current_dictogram.return_weighted_random_word()
    current_word =  random_weighted_word
    # print 'current word: ' + current_word
    sentence.append(current_word)

print sentence
