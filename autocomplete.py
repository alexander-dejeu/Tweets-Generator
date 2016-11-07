import sys
from datetime import datetime

_end = '_end_'

def make_dictionary_trie():
    # Open the dictionary
    # dictionary_file = open('/usr/share/dict/words', 'r')
    dictionary_file = open('small_dictionary.txt', 'r')
    all_words = dictionary_file.read().splitlines()

    trie_root = dict()

    for word in all_words:
        current_node = trie_root
        for letter in word:
            current_node = current_node.setdefault(letter, {})
        current_node[_end] = _end


    # Done with the dictionary - close it
    dictionary_file.close()
    print trie_root
    return trie_root


def search_trie_for(trie, prefix):
    current_node = trie
    for letter in prefix:
        if letter in current_node:
            current_node = current_node[letter]
        else:
            return False
    else:
        if _end in current_node:
            return True
        else:
            return False


def main():
    base_start_time = datetime.now()
    tree = make_dictionary_trie()
    base_end_time = datetime.now()
    base_run_time = base_end_time - base_start_time
    print 'Time to create the prefix tree : ', base_run_time

    user_argument_count = len(sys.argv)
    if user_argument_count == 1:
        print 'Error: word not provided'
    else:
        user_autocomplete_word = str(sys.argv[1])
        search_trie_for(tree, user_autocomplete_word)

main()
