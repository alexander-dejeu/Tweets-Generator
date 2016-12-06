import sys
import random
from operator import itemgetter
import timeit

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

    def return_random_word(self):
        # Another way:  Should test: random.choice(histogram.keys())
        random_key = random.sample(self, 1)
        return random_key[0]

    def return_weighted_random_word(self):
        # Step 1: Generate random number between 0 and total count - 1
        random_int = random.randint(0, self.tokens-1)
        index = 0
        list_of_keys = self.keys()
        # print 'the random index is:', random_int
        for i in range(0, self.types):
            index += self[list_of_keys[i]]
            # print index
            if(index > random_int):
                # print list_of_keys[i]
                return list_of_keys[i]


# *************** DICTIONARY HISTOGRAM *************** #
# *************** DICTIONARY TESTS *************** #

class Listogram(list):

    def __init__(self, iterable=None):
        """Initialize this histogram as a new list; update with given items"""
        super(Listogram, self).__init__()
        self.types = 0  # the number of distinct item types in this histogram
        self.tokens = 0  # the total count of all item tokens in this histogram
        if iterable:
            self.update(iterable)
        self.sort_self_linear()

    def sort_self_linear(self):
        self = sorted(self, key=itemgetter(1), reverse=True)

    def binary_self(self):
        self.sort_self_linear()
        right_index = -1
        print self.tokens
        for i in range(0, self.types):
            right_index = right_index + self[i][1]
            self[i] = (self[i][0], right_index)

    def update(self, iterable):
        """Update this histogram with the items in the given iterable"""
        # foo[1] = ('b','friend')
        for item in iterable:
            index = self._index(item)
            if index is None:
                self.append((item, 1))
                self.types += 1
                self.tokens += 1
            else:

                self[index] = (self[index][0], self[index][1] + 1)
                count = self[index][1]
                self[index] = (item, count + 1)
                self.tokens += 1

    def count(self, item):
        """Return the count of the given item in this histogram, or 0"""
        index = self._index(item)
        if index is None:
            return 0
        return self[index][1]

    def __contains__(self, item):
        """Return True if the given item is in this histogram, or False"""

        if self._index(item) is None:
            return False
        return True

    def _index(self, target):
        """Return the index of the (target, count) entry if found, or None"""
        for index, (word, count) in enumerate(self):
            if word == target:
                return index
        return None

        for index in range(0, len(self)):
            if self[index][0] == target:
                return index
        return None

    def weighted_random_word_tuple(self):
        type_count = len(histogram)
        # Step 2: Generate random number between 0 and total count - 1
        random_int = random.randint(0, self.tokens-1)
        index = 0
        # print 'the random index is:', random_int
        for i in range(0, self.types):
            index += self[i][1]
            # print index
            if(index > random_int):
                # print list_of_keys[i]
                return self[i][0]

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

    def binary_search_random_word_tuple(histogram):
        # Step 1: Get total count of all words in histogram
        # print histogram
        type_count = len(histogram)
        # +1 because it [1] is the index of the furtherest right element
        token_count = histogram[type_count-1][1] + 1
        # Step 2: Generate random number between 0 and total count - 1
        random_int = random.randint(0, self.tokens-1)

        word = binary_search(self, self.types, self.types/2, random_int)
        return word

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


    # if(histogram[histogram_keys[key_count/2] ==  )





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

def test_weighted_random_word(histogram, times):
    results = dict()
    for i in range(0, times):
        result = histogram.return_weighted_random_word()
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

# def random_word():
#     file_name = 'small_text_sample.txt'
#     histogram_data = tuple_histogram_sorted(file_name)
#     return weighted_random_word_tuple(histogram_data)
#
#
# def random_sentence():
#     file_name = 'small_text_sample.txt'
#     histogram_data = tuple_histogram_sorted(file_name)
#     return weighted_random_word_tuple(histogram_data)

def list_of_words(length):
    dict_words = '/usr/share/dict/words'
    words_str  = open(dict_words, 'r').read()
    all_words  = words_str.split("\n")
    return all_words[0:length]

def main():
    file_name = 'steve_jobs_speech.txt'
    print '*********** GETTING DATA ***********'
    print 'Start reading/parsing file'


    data_file = open(file_name, 'r')
    words_list = data_file.read().split()
    for word in words_list:
        word = word.decode('utf-8').lower().encode('utf-8')

    total_read_parse_time = 3
    print 'Finished reading/parsing file in: ', total_read_parse_time, 'seconds'

    hundred_words = list_of_words(100)
    ten_thousand_words = list_of_words(10000)

    hundred_hgram = Dictogram(hundred_words)
    ten_thousand_hgram = Dictogram(ten_thousand_words)
    hundred_search = hundred_words[-1]
    ten_thousand_search = ten_thousand_words[-1]
    stmt = "count('{}', hundred_hgram)".format(hundred_search)
    setup = "from __main__ import count, hundred_hgram"
    timer = timeit.Timer(stmt, setup=setup)

    iterations = 10000
    result = timer.timeit(number=iterations)
    print("count time for 100-word histogram: " + str(result))

    '*********** CREATING DATA STRUCTURES ***********'
    'Start creating Dictogram'
    dictogram = Dictogram(words_list)
    'Time to create Dictogram: ', 'seconds'


    listogram = Listogram(words_list)
    'Time to create Listogram: ', 'seconds'

    listogram_sorted = Listogram(words_list)
    listogram_sorted.sort_self_linear()
    'Time to create sorted Listogram: ', 'seconds'

    listogram_binary = Listogram(words_list)
    listogram_binary.binary_self()
    'Time to create binary searchable Listogram: ', 'seconds'


    'Time to create HashTable: ', 'seconds'


    '*********** TESTING TIME TO GET LENGTH ***********'
    'Time to get length of Dictogram: ', 'seconds'
    'Time to get length of Listogram: ', 'seconds'
    'Time to get length of sorted Listogram: ', 'seconds'
    'Time to get length of binary searchable Listogram: ', 'seconds'
    'Time to get length of HashTable', 'seconds'



    '*********** TESTING TIME TO GET RANDOM WEIGHTED WORD ***********'
    'In these tests the functions are run 10000 times and then the average is calculated'
    'Time to get random weighted word -> dictogram: '
    # print weighted_random_word_tuple(histogram_data)
    test_weighted_random_word(dictogram, 10000)
    # print unique_words(histogram_data)
    # print frequency(histogram_data, 'all')


if __name__ == '__main__':
    main()
