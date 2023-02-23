# Author: Delainee Lenss
# GitHub username: delainee64
# Date: 02/19/2023
# Description: Write a LinkedList class that has recursive implementations of the
# add and remove methods described in the Exploration. It should also have
# recursive implementations of the contains, insert, and reverse methods
# described in the exercises.

class Node:
    """Represents a node is a linked list."""

    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        """Returns data for the node."""
        return self.data

    def set_data(self, newData):
        """Sets data for the node."""
        self.data = newData

    def get_next(self):
        """Returns the next node."""
        return self.next

    def set_next(self, newNode):
        """Sets the next node."""
        self.next = newNode


class LinkedList:
    """A linked list implementation of the List ADT."""

    def __init__(self):
        self._head = None

    def get_head(self):
        """Returns the head of the node."""
        return self._head

    def rec_add(self, value, a_node):
        """A recursive function to a new node in the linked list. """
        if a_node is None:
            return Node(value)
        else:
            a_node.set_next(self.rec_add(value, a_node.get_next()))
            return a_node

    def add(self, value):
        """Adds a value to a new node in the linked list."""
        self._head = self.rec_add(value, self._head)

    def rec_remove(self, value, a_node):
        """A recursive function of removing a value from the linked list."""
        if a_node is None:
            return a_node
        if a_node.get_data() == value:
            return a_node.get_next()
        else:
            a_node.set_next(self.rec_remove(value, a_node.get_next()))
            return a_node

    def remove(self, value):
        """A function that helps removes a value from the linked list."""
        self._head = self.rec_remove(value, self._head)

    def rec_contains(self, value, a_node):
        """A recursive function to check whether a value is in the list."""
        if a_node is None:
            return False
        if a_node.get_data() == value:
            return True
        return self.rec_contains(value, a_node.get_next())

    def contains(self, value):
        """A function to help the recursive function check the contents of the list."""
        return self.rec_contains(value, self._head)

    def rec_to_plain_list(self, a_node):
        """A recursive function that returns a regular Python list."""
        if a_node is None:
            return []
        return [a_node.get_data()] + self.rec_to_plain_list(a_node.get_next())

    def insert(self, value, pos):
        """Adds a node containing val to the linked list """
        self._head = self.rec_insert(self._head, value, pos)

    def rec_insert(self, a_node, value, pos):
        """Adds a node containing val to the linked list """
        if a_node is None and pos > 0:
            return a_node
        if pos == 0:
            node = Node(value)
            node.set_next = a_node
            return node
        node = self.rec_insert(a_node.get_next(), value, pos - 1)
        a_node.set_next(node)
        return a_node

    def to_plain_list(self):
        """A recursive function that returns a regular Python list."""
        return self.rec_to_plain_list(self._head)

    def rec_reverse(self, a_node):
        """A recursive function that rearranges the order of the nodes."""
        if a_node is None:
            return a_node
        if a_node.get_next() is None:
            return a_node
        rem_node = self.rec_reverse(a_node.get_next())
        a_node.get_next().set_next(a_node)
        a_node.set_next(None)
        return rem_node

    def reverse(self):
        """A function that helps rearrange the order of the nodes. """
        self._head = self.rec_reverse(self._head)


# new = LinkedList()
# for val in range(8):
    # new.add(val + 1)

# print(new.to_plain_list())
# new.remove(2)
# new.insert(1, 3)
# print(new.to_plain_list())
# print(new.contains(3))
# print(new.contains(4))
# print(new.contains(5))
# print(new.to_plain_list())
