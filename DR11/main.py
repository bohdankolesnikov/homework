# 16.11

class StringIterator:

    def __init__(self, st):
        self.__array = st.split();
        self.__tarray = st.split();

    def __iter__(self):
        return iter(self.__tarray);

    def set_direct_order(self):
        self.__tarray = self.__array;

    def set_reverse_order(self):
        self.__tarray = self.__array[::-1];

    def set_uplen_order(self):
        self.__tarray = sorted(self.__array, key=len);

    def set_downlen_order(self):
        self.__tarray = sorted(self.__array, key=len)[::-1];

    def set_palindrome(self):
        self.__tarray = list(filter(is_palindrome, self.__array));


def is_palindrome(st):
    return st == st[::-1];
