import sys


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
        print word

    histogram = dict()

    for word in words_list:
        if word in histogram:
            histogram[word] += 1
        else:
            histogram[word] = 1

    print histogram['all']
    print 'ima histogram.'

'''
A function that takes a histogram argument and returns the total count of
unique words in the histogram. For example, when given the histogram
for The Adventures of Sherlock Holmes, it returns the integer 8475.
'''
def unique_words():
    return 1

'''
A function that takes a word and histogram argument and returns the number of
times that word appears in a text. For example, when given the word "mystery"
and the Holmes histogram, it will return the integer 20.
'''
def frequency():
    return 1


def main():
    file_name = 'steve_jobs_speech.txt'
    histogram(file_name)

main()
