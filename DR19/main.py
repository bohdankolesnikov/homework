# 19.17

import time;
from collections import defaultdict

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
class Polynome(defaultdict):

    def __init__(self, **kwargs):
        defaultdict.__init__(self, float, **kwargs);

    def fromstring(s):

        p = Polynome();
        s = s.replace("+", ' ');
        ls = s.split();
        for m in ls:
            c = m.split('*x**');
            k = int(c[1]);
            v = float(c[0]);
            p[k] = v;

        return p;

    fromstring = staticmethod(fromstring);

    def add_monom(self, deg, coeff):

        if (coeff != 0):
            self[deg] += coeff;

    def get_degree(self):

        return max(self);

    def __str__(self):

        monomials = list(self.items());
        if (not monomials):
            poly_str = "0.0*x**0";
        else:
            monomials.sort(reverse=True);
            ls = ["{}*x**{}".format(mono[1], mono[0]) for mono in monomials];
            poly_str = ' + '.join(ls);

        return poly_str;

    def __call__(self, x):

        return sum([self[k]*x**k for k in self]);

    def __add__(self, other):

        p = Polynome();

        keys = set(self.keys()) | set(other.keys());

        for k in keys:
            p[k] = self[k] + other[k];

        return self._delzeroes(p);

    def __radd__(self, other):

        return self.__add__(other);

    def __sub__(self, other):

        p = Polynome();
        
        keys = set(self.keys()) | set(other.keys());

        for k in keys:
            p[k] = self[k] - other[k];
        
        return self._delzeroes(p);

    def __rsub__(self, other):

        p = Polynome();

        keys = set(self.keys()) | set(other.keys());

        for k in keys:
            p[k] = other[k] - self[k];

        return self._delzeroes(p);

    def __mul__(self, other):

        p = Polynome();

        for k1 in self:
            for k2 in other:
                p[k1 + k2] += self[k1] * other[k2];

        return self._delzeroes(p);

    def __rmul__(self, other):

        return self.__mul__(other);

    def deriv(self, n=1):

        p = self;

        for i in range(n):
            p = self._deriv(p);

        return self._delzeroes(p);

    def _deriv(self, p):

        pp = Polynome();

        for k in p:
            if (k != 0):
                pp[k - 1] = p[k] * k;

        return pp;

    def _delzeroes(self, p):

        pp = Polynome();

        for k in p:
            if (p[k] != 0):
                pp[k] = p[k];

        return pp;

if (__name__ == "__main__"):
    p1 = Polynome.fromstring("5.2*x**4 + -0.5*x**3 + 1*x**2 + 10*x**0");
    print(f"p1 = {p1}");
    p2 = Polynome.fromstring("3*x**5 + 10*x**3 + -5*x**2 + 0.2*x**1 + 0.2*x**0");
    print("p2 = ", p2);

    print(p1 + p2);
