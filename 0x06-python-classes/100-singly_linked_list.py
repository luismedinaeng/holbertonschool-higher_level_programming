#!/usr/bin/python3
class Node:
    def __init__(self, data, next_node=None):
        if type(data) != int:
            raise TypeError("data must be an integer")
        self.__data = data
        if next_node is not None and type(next_node) != Node:
            raise TypeError("next_node must be a Node object")
        self.__next_node = next_node

    @property
    def data(self):
        ''' Returns the data of the node
        '''
        return self.__data

    @data.setter
    def data(self, value):
        ''' Checks the type of the data and update its value
        '''
        if type(data) != int:
            raise TypeError("data must be an integer")
        self.__data = data

    @property
    def next_node(self):
        ''' Returns the next node
        '''
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        ''' Checks the type of the next node and update its value
        '''
        if value is not None and type(value) != Node:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

class SinglyLinkedList:
    def __init__(self):
        self.__head = None

    def __str__(self):
        current = self.__head
        txt = ""
        while current is not None:
            txt = txt + str(current.data)
            if current.next_node is not None:
                txt = txt + "\n"
            current = current.next_node
        return txt

    def sorted_insert(self, value):
        ''' Inserts a new node into the correct sorted position in the list
        '''
        if self.__head is None:
            self.__head = Node(value)
        elif self.__head.data > value:
            self.__head = Node(value, self.__head)
        else:
            current = self.__head
            while current is not None:
                if current.next_node is None:
                    current.next_node = Node(value)
                    return
                if current.next_node.data > value:
                    current.next_node = Node(value, current.next_node)
                    return
                current = current.next_node
