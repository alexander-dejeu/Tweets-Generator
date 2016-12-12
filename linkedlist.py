#!python

from __future__ import print_function


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data"""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node"""
        return 'Node({})'.format(repr(self.data))


class LinkedList(object):

    def __init__(self, iterable=None):
        """Initialize this linked list; append the given items, if any"""
        self.head = None
        self.tail = None
        if iterable:
            for item in iterable:
                self.append(item)

    def __repr__(self):
        """Return a string representation of this linked list"""
        return 'LinkedList({})'.format(self.as_list())

    def __iter__(self):
        """Make the linkedList an iterable
        Best case running time: N(n-m) where m is the amount of remained
        Worst case running time: O(n) has to iterate through every item.
        """
        current = self.head
        while current is not None:
            yield current
            current = current.next

    def as_list(self):
        """Return a list of all items in this linked list
        Best case running time: N(n) has to iterate through every item.
        Worst case running time: O(n) has to iterate through every item.
        """
        result = []
        current = self.head
        while current is not None:
            result.append(current.data)
            # result.append(current)
            current = current.next
        return result

    def is_empty(self):
        """Return True if this linked list is empty, or False
        Best case running time: N(1) has to just check the head (one item)
        Worst case running time: O(1) constant because it is always only
        checking one thing.
        """
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes
        Best case running time: N(n) has to iterate through every node
        Worst case running time: O(n) has to iterate through every node
        """
        # TODO: count number of items
        count = 0
        current_node = self.head
        while current_node is not None:
            count += 1
            current_node = current_node.next
        return count

    def append(self, item):
        """Insert the given item at the tail of this linked list
        Return the length of this linked list by traversing its nodes
        Best case running time: N(1) contant - just adding to the tail node
        Worst case running time: O(1) contant - just adding to the tail node
        """
        # TODO: append given item
        # If the head is None then this is first item being added
        if self.head is None:
            self.head = Node(item)
            self.tail = self.head
        # If the head and tail equal eachother then there should only be one
        # element.
        elif self.head == self.tail:
            self.tail = Node(item)
            self.head.next = self.tail
        # All other cases should just update the old and new tail data
        else:
            new_tail = Node(item)
            self.tail.next = new_tail
            self.tail = new_tail

    def prepend(self, item):
        """Insert the given item at the head of this linked list
        Return the length of this linked list by traversing its nodes
        Best case running time: N(1) contant - just moving head node
        Worst case running time: O(1) contant - just moving the head node
        """
        # TODO: prepend given item
        if self.head is None:
            self.head = Node(item)
            self.tail = self.head
        elif self.head == self.tail:
            self.head = Node(item)
            self.head.next = self.tail
        else:
            new_head = Node(item)
            new_head.next = self.head
            self.head = new_head

    def delete(self, item):
        """Delete the given item from this linked list, or raise KeyError
        Return the length of this linked list by traversing its nodes
        Best case running time: N(1) first element is the one to delete
        Worst case running time: O(n) last node is the one to delete - has to
        itterate through all of the nodes
        ['hi', 'my', 'name']
        [('hi', 3), ()]
        """
        # TODO: find given item and delete if found
        current_node = self.head

        if current_node is None:
            raise KeyError('could not find %c in LinkedList' % (item))

        comparison = lambda node: node.data == item
        if isinstance(current_node.data, tuple):
            comparison = lambda node: node.data[0] == item

        if comparison(self.head) and self.head == self.tail:
            self.head = current_node.next
            self.tail = self.head
            return
        elif comparison(self.head):
            self.head = current_node.next
            return
        else:
            while current_node.next is not None:
                if comparison(current_node.next):
                    if current_node.next == self.tail:
                        self.tail = current_node
                        current_node.next = current_node.next.next
                        return

                    current_node.next = current_node.next.next
                    return
                current_node = current_node.next

            raise KeyError('could not find %c in LinkedList' % (item))

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality
        Return the length of this linked list by traversing its nodes
        Best case running time: N(1) first element is the one to find
        Worst case running time: (n) last node is the one to find - has to
        itterate through all of the nodes
        """
        # TODO: find item where quality(item) is True
        current_node = self.head

        while current_node is not None:
            if quality(current_node.data):
                return current_node.data
            current_node = current_node.next

        return None


def test_linked_list():
    ll = LinkedList()
    print(ll)
    ll.append('A')
    print(ll)
    ll.append('B')
    print(ll)
    ll.append('C')
    print('iterable testing:')
    for node in ll:
        print(node)
        print(node.data)
        print(node.next)
    print('done testing interable')
    print(ll)
    print('head: ' + str(ll.head))
    print('tail: ' + str(ll.tail))
    print(ll.length())

    ll.delete('A')
    print(ll)
    ll.delete('C')
    print(ll)
    ll.delete('B')
    print(ll)
    print('head: ' + str(ll.head))
    print('tail: ' + str(ll.tail))
    print(ll.length())


if __name__ == '__main__':
    test_linked_list()
