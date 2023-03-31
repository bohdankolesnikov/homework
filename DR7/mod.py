import math

class Point2:

    def __init__(self, x, y):
        self._x = x;
        self._y = y;

    def get_x(self):
        return self._x;

    def get_y(self):
        return self._y;

    def __str__(self):
        return "({}, {})".format(self._x, self._y);


class Segment:

    def __init__(self, a, b):
        self._a = a;
        self._b = b;

    def get_a(self):
        return self._a;

    def get_b(self):
        return self._b;

    def __str__(self):
        return "[{}, {}]".format(self._a, self._b);

    def len(self):
        return math.sqrt( (self._a.get_x() - self._b.get_x())**2 + (self._a.get_y() - self._b.get_y())**2 );


class SegmentEx(Segment):


    def __eq__(self, seg):
        return self.len() == seg.len();

    def __ne__(self, seg):
        return self.len() != seg.len();

    def __lt__(self, seg):
        return self.len() < seg.len();

    def __le__(self, seg):
        return self.len() <= seg.len();

    def __gt__(self, seg):
        return self.len() > seg.len();

    def __ge__(self, seg):
        return self.len() >= seg.len();
