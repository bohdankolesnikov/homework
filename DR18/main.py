# 19.7

import time;


def get_methods(cls):
    m_lst = [];
    for key in cls.__dict__:
        if ("__call__" in dir(cls.__dict__[key])):       # якщо можна викликати, то є методом
            m_lst = m_lst + [cls.__dict__[key]];

    return m_lst;


def decorator(cls):

    def _wrapper(f):

        def __wrapper(*args, **kwargs):

            start = time.time();

            print(f"calling {f.__name__}");

            res = f(*args, **kwargs);

            print(f"called {f.__name__}, time of execution: {time.time() - start}");

            return res;

        return __wrapper;

    cls_methods = get_methods(cls);

    for key in cls.__dict__:
        if (cls.__dict__[key] in cls_methods):
            setattr(cls, key, _wrapper(cls.__dict__[key]));         # еквівалентно cls.key = _wrapper(cls.__dict__[key]);

    return cls;

@decorator
class Btree:
    
    def __init__(self):
        self._data = None;
        self._ls = None;
        self._rs = None;

    def isempty(self):
        return self._data == None and self._ls == None and self._rs == None;

    def maketree(self, data, t1, t2):
        self._data = data;
        self._ls = t1;
        self._rs = t2;

    def root(self):
        if self.isempty():
            print("root: Дерево порожнє");
            exit(1);
        return self._data;

    def leftson(self):
        if self.isempty():
            t = self;
        else:
            t = self._ls;
        return t;

    def rightson(self):
        if self.isempty():
            t = self;
        else:
            t = self._rs;
        return t;

    def updateroot(self, data):
        if self.isempty():
            self._ls = Btree();
            self._rs = Btree();
        self._data = data;

    def updateleft(self, t):
        self._ls = t;

    def updateright(self, t):
        self._rs = t;

if __name__ == "__main__":
    tr = Btree();
    tr.maketree(10, Btree().maketree(9, Btree().updateroot(4), Btree().updateroot(17)), Btree().updateroot(22));
