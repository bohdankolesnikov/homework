class Deque:

    def __init__(self):
        self.__array = [];

    def push_back(self, elem):
        self.__array = self.__array + [elem];

    def push_front(self, elem):
        self.__array = [elem] + self.__array;

    def pop_back(self):
        if (self.is_empty()):
            raise Exception("deque is empty");
        else:
            elem = self.__array[-1];
            self.__array = self.__array[:-1];
            return elem;

    def pop_front(self):
        if (self.is_empty()):
            raise Exception("deque is empty");
        else:
            elem = self.__array[0];
            self.__array = self.__array[1:];
            return elem;

    def is_empty(self):
        return (len(self.__array) == 0);

class Stack:

    def __init__(self):
        self.__deque = Deque();

    def push(self, elem):
        self.__deque.push_back(elem);

    def pop(self):
        if (self.__deque.is_empty()):
            raise Exception("stack is empty");
        else:
            return self.__deque.pop_back();

    def is_empty(self):
        return self.__deque.is_empty();
