#!python

from linkedlist import LinkedList


class HashTable(object):

    def __init__(self, init_size=2000):
        """Initialize this hash table with the given initial size"""
        self.buckets = [LinkedList() for i in range(init_size)]

    def __repr__(self):
        """Return a string representation of this hash table"""
        return 'HashTable({})'.format(self.length())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored
        Best case running time: N(1) constant
        Worst case running time: O(1)  """
        return hash(key) % len(self.buckets)

    def length(self):
        """Return the length of this hash table by traversing its buckets
        Best case running time: N(n) has to iterate through every item in all
        linkedLists.
        Worst case running time: O(n) has to iterate through every item in all
        linkedLists.
        """
        # TODO: Count number of key-value entries in each of the buckets
        length = 0
        for bucket in self.buckets:
            length += bucket.length()
        return length

    def contains(self, key):
        """Return True if this hash table contains the given key, or False
        Best case running time: N(2n) 2 O(n) opperations are completed with
        the bucket index and finding the key
        Worst case running time: 2 O(n) opperations are completed with
        the bucket index and finding the key
        """
        # TODO: Check if the given key exists in a bucket
        bucket_index = self._bucket_index(key)
        maybe_key = self.buckets[bucket_index].find(lambda x: x[0] == key)
        if maybe_key is not None:
            return True
        return False

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError
        Best case running time: N(2n) 2 O(n) opperations are completed with
        the bucket index and finding the key
        Worst case running time: 2 O(n) opperations are completed with
        the bucket index and finding the key
        """
        # TODO: Check if the given key exists and return its associated value
        bucket_index = self._bucket_index(key)
        maybe_value = self.buckets[bucket_index].find(lambda x: x[0] == key)
        print key, maybe_value
        if maybe_value is not None:
            return maybe_value[1]
        raise (KeyError, 'Key not found')

    def set(self, key, value):
        """Insert or update the given key with its associated value
        Best case running time: N(2n) 2 O(n) opperations are completed with
        the bucket index and finding the key
        Worst case running time: 2 O(n) opperations are completed with
        the bucket index and finding the key
        """
        # TODO: Insert or update the given key-value entry into a bucket
        bucket_index = self._bucket_index(key)
        maybe_value = self.buckets[bucket_index].find(lambda x: x[0] == key)
        if maybe_value is not None:
            print 'THE VALUE IS: ', maybe_value
            self.delete(key)
        # print maybe_value
        self.buckets[bucket_index].append((key, value))

    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError
        Best case running time: N(2n) 2 O(n) opperations are completed with
        the bucket index and finding the key
        Worst case running time: 2 O(n) opperations are completed with
        the bucket index and finding the key"""
        # TODO: Find the given key and delete its entry if found
        bucket_index = self._bucket_index(key)
        print 'bucket', self.buckets[bucket_index]
        print 'key', key
        self.buckets[bucket_index].delete(key)
        # self.buckets[bucket_index].find(lambda x: x[0] == key)
        # if maybe_delete is not None:
        #      self.buckets[bucket_index].delete(key)
        # raise (KeyError, 'key not present!')

    def keys(self):
        """Return a list of all keys in this hash table
        Best case running time: N(1) Only one item in the bucket
        Worst case running time: O(n) has to go through all the LL and nodes
        to get all keys
        """
        # TODO: Collect all keys in each of the buckets
        all_keys_list = []
        for bucket in self.buckets:
            for item in bucket:
                print item
                all_keys_list.append(item.data[0])
        return all_keys_list

    def values(self):
        """Return a list of all values in this hash table
        Best case running time: N(1) Only one item in the bucket
        Worst case running time: O(n) has to go through all the LL and nodes
        to get all keys
        """
        # TODO: Collect all values in each of the buckets
        all_values_list = []
        for bucket in self.buckets:
            for item in bucket:
                all_values_list.append(item.data[1])
        return all_values_list
