import sys
import random
from operator import itemgetter

class Dictogram(dict):
    def __init__(self, iterable=None):
        """Initialize this histogram as a new dict; update with given items"""
        super(Dictogram, self).__init__()
        self.types = 0  # the number of distinct item types in this histogram
        self.tokens = 0  # the total count of all item tokens in this histogram
        if iterable:
            self.update(iterable)

    def update(self, iterable):
        """Update this histogram with the items in the given iterable"""
        for item in iterable:
            if item in self:
                self[item] += 1
                self.tokens += 1
            else:
                self[item] = 1
                self.types += 1
                self.tokens += 1

    def count(self, item):
        """Return the count of the given item in this histogram, or 0"""
        if item in self:
            return self[item]
        return 0



# *************** HELPERS DICTIONARY *************** #
def unique_words(histogram):
    '''
    A function that takes a histogram argument and returns the total count of
    unique words in the histogram. For example, when given the histogram
    for The Adventures of Sherlock Holmes, it returns the integer 8475.
    '''
    return len(histogram)


def frequency(histogram, word):
    '''
    A function that takes a word and histogram argument and returns the number
    of times that word appears in a text. For example, when given the word
    "mystery" and the Holmes histogram, it will return the integer 20.
    '''
    return histogram[word]


def return_random_word(histogram):
    # Another way:  Should test: random.choice(histogram.keys())
    random_key = random.sample(histogram, 1)
    return random_key[0]


def get_token_count(histogram):
    sum = 0
    for key in histogram:
        sum += histogram[key]
    return sum


def return_weighted_random_word(histogram):
    # Step 1: Get total count of all words in histogram
    # print histogram
    token_count = get_token_count(histogram)
    type_count = len(histogram.keys())
    # Step 2: Generate random number between 0 and total count - 1
    random_int = random.randint(0, token_count-1)
    index = 0
    list_of_keys = histogram.keys()
    # print 'the random index is:', random_int
    for i in range(0, type_count):
        index += histogram[list_of_keys[i]]
        # print index
        if(index > random_int):
            # print list_of_keys[i]
            return list_of_keys[i]


# *************** DICTIONARY HISTOGRAM *************** #
def histogram(file_name):
    '''
    A function which takes a source_text argument (can be either a filename or
    the contents of the file as a string, your choice) and return a histogram
    data structure that stores each unique word along with the number of times
    the word appears in the source text.
    '''
    data_file = open(file_name, 'r')
    words_list = data_file.read().split()
    for word in words_list:
        word = word.decode('utf-8').lower().encode('utf-8')
        # print word

    histogram = dict()

    for word in words_list:
        if word in histogram:
            histogram[word] += 1
        else:
            histogram[word] = 1
    return histogram


# *************** DICTIONARY TESTS *************** #
def test_weighted_random_word(histogram, times):
    results = dict()
    for i in range(0, times):
        result = return_weighted_random_word(histogram)
        if result in results:
            results[result] += 1
        else:
            results[result] = 1
    # Organize results to display most common first
    results_tuple = results.items()
    # Slower version according to SO
    # sorted_results = sorted(results_tuple, key=lambda x: x[1], reverse=True)
    sorted_results = sorted(results_tuple, key=itemgetter(1), reverse=True)

    print sorted_results


# *************** HELPERS TUPLE *************** #
def get_token_count_tuple(histogram):
    sum = 0
    for i in range(0, len(histogram)):
        sum += histogram[i][1]
    return sum


def weighted_random_word_tuple(histogram):
    # Step 1: Get total count of all words in histogram
    # print histogram
    token_count = get_token_count_tuple(histogram)
    type_count = len(histogram)
    # Step 2: Generate random number between 0 and total count - 1
    random_int = random.randint(0, token_count-1)
    index = 0
    # print 'the random index is:', random_int
    for i in range(0, type_count):
        index += histogram[i][1]
        # print index
        if(index > random_int):
            # print list_of_keys[i]
            return histogram[i][0]


# *************** TUPLE HISTOGRAM *************** #
def tuple_histogram(file_name):
    dict_historgram = histogram(file_name)
    # print 'dict_historgram:', dict_historgram
    tuple_histogram = dict_historgram.items()
    # print tuple_histogram
    return tuple_histogram


# *************** SORTED TUPLE HISTOGRAM *************** #
def tuple_histogram_sorted(file_name):
    tup_histogram = tuple_histogram(file_name)
    return sorted(tup_histogram, key=itemgetter(1), reverse=True)


# *************** TUPLE TESTS *************** #
def test_weighted_random_word_tuple(histogram, times):
    results = dict()
    for i in range(0, times):
        result = weighted_random_word_tuple(histogram)
        if result in results:
            results[result] += 1
        else:
            results[result] = 1
    # Organize results to display most common first
    results_tuple = results.items()
    # Slower version according to SO
    # sorted_results = sorted(results_tuple, key=lambda x: x[1], reverse=True)
    sorted_results = sorted(results_tuple, key=itemgetter(1), reverse=True)

    print sorted_results


# *************** BINARY TUPLE HISTOGRAM HELPERS *************** #
def binary_search(histogram, key_count, current_index, target):
    # Alex Dog Charlie Bob
    #  3    6     8    9
    if current_index == 0:
        return histogram[0][0]

    lower_bound = histogram[current_index-1][1]

    if histogram[current_index][1] >= target and lower_bound < target:
        word = histogram[current_index][0]
        return word
    elif histogram[current_index][1] < target:
        new_index = current_index + (key_count - current_index)/2
        return binary_search(histogram, key_count, new_index, target)
    elif histogram[current_index][1] > target:
        new_index = current_index - (key_count - current_index)/2
        return binary_search(histogram, key_count, new_index, target)
    else:
        print 'didnt account for something lamo'

    # if(histogram[histogram_keys[key_count/2] ==  )


def binary_search_random_word_tuple(histogram):
    # Step 1: Get total count of all words in histogram
    # print histogram
    type_count = len(histogram)
    # +1 because it [1] is the index of the furtherest right element
    token_count = histogram[type_count-1][1] + 1
    # Step 2: Generate random number between 0 and total count - 1
    random_int = random.randint(0, token_count-1)

    word = binary_search(histogram, type_count, type_count/2, random_int)
    return word


# *************** BINARY TUPLE HISTOGRAM TESTS *************** #
def test_binary_search(histogram, times):
    results = dict()
    for i in range(0, times):
        result = binary_search_random_word_tuple(histogram)
        if result in results:
            results[result] += 1
        else:
            results[result] = 1
    # Organize results to display most common first
    results_tuple = results.items()
    # Slower version according to SO
    # sorted_results = sorted(results_tuple, key=lambda x: x[1], reverse=True)
    sorted_results = sorted(results_tuple, key=itemgetter(1), reverse=True)

    print sorted_results


# *************** BINARY HISTOGRAM *************** #
def binary_histogram(file_name):
    sorted_historgram = tuple_histogram_sorted(file_name)
    right_index = -1
    for i in range(0, len(sorted_historgram)):
        right_index = right_index + sorted_historgram[i][1]
        sorted_historgram[i] = (sorted_historgram[i][0], right_index)

    return sorted_historgram


def random_word():
    file_name = 'small_text_sample.txt'
    histogram_data = tuple_histogram_sorted(file_name)
    return weighted_random_word_tuple(histogram_data)


def random_sentence(data_structure):
    sentence = []
    for i in range(0, 20):
        sentence.append(return_weighted_random_word(data_structure))

    return ' '.join(sentence)

def random_actor():
    file_name = 'SiliconValley_Actors.txt'
    data_file = open(file_name, 'r')
    actor_list = data_file.read().split('\n')
    random_actor = actor_list[random.randint(0, len(actor_list)-2)]
    return random_actor

def main():
    file_name = 'small_text_sample.txt'
    histogram_data = binary_histogram(file_name)
    # print histogram_data
    # print return_random_word(histogram_data)
    random_sentence()
    random_actor2 = random_actor()
    print('Yo random Actor: ', random_actor2)

    random_actor_cleaned = random_actor2.replace(' ', '')
    random_actor_cleaned = random_actor_cleaned.replace('\'', '')
    print('random actor cleaned ', random_actor_cleaned)
    print "images/"+random_actor_cleaned+".png"

    # print weighted_random_word_tuple(histogram_data)
    test_binary_search(histogram_data, 10000)
    # print unique_words(histogram_data)
    # print frequency(histogram_data, 'all')


if __name__ == '__main__':
    main()
