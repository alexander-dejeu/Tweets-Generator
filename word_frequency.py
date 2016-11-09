import sys
import random


def return_random_word(histogram):
    # Another way:  Should test: random.choice(histogram.keys())
    random_key = random.sample(histogram, 1)
    return random_key[0]


def tuple_histogram(fime_name):
    # NOT WORKING
    data_file = open(file_name, 'r')
    words_list = data_file.read().split()
    for word in words_list:
        word = word.decode('utf-8').lower().encode('utf-8')
        print word
        print zip(word_list)
    histogram = list()
    for word in word_list:
        if word in histogram:
            print 'done'

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


def unique_words(histogram):
    '''
    A function that takes a histogram argument and returns the total count of
    unique words in the histogram. For example, when given the histogram
    for The Adventures of Sherlock Holmes, it returns the integer 8475.
    '''
    return len(histogram)


def frequency(histogram, word):
    '''
    A function that takes a word and histogram argument and returns the number of
    times that word appears in a text. For example, when given the word "mystery"
    and the Holmes histogram, it will return the integer 20.
    '''
    return histogram[word]



def main():
    file_name = 'steve_jobs_speech.txt'
    histogram_data = histogram(file_name)
    print return_random_word(histogram_data)
    # print unique_words(histogram_data)
    # print frequency(histogram_data, 'all')


main()
