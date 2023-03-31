# 13.9вг

import math

class Point:

    def __init__(self, x, y):
        self.set(x, y);

    def get(self):
        return (self.__x, self.__y);

    def set(self, x, y):
        self.__x = x;
        self.__y = y;

    def show(self):
        print(f"({self.__x}, {self.__y})");


class LineSegment:

    def __init__(self, a, b):
        self.set(a, b);

    def get(self):
        return (self.__a, self.__b);

    def set(self, a, b):
        self.__a = a;
        self.__b = b;

    def show(self):
        print(f"[{self.__a.get()}, {self.__b.get()}]");

    def leng(self):
        return math.sqrt(math.pow(self.__a.get()[0] - self.__b.get()[0], 2) + math.pow(self.__a.get()[1] - self.__b.get()[1], 2));

    def on_line(self, pt):
        # is vertical?
        if (self.__a.get()[0] == self.__b.get()[0]):
            if (pt.get()[0] == self.__a.get()[0]):
                return True;
            else:
                return False;
        else:
            # a = (xa, ya), b = (xb, yb)
            # y = k*x + b
                # k = (yb - ya) / (xb - xa)
                # b = -k * xa + ya
            k = (self.__b.get()[1] - self.__a.get()[1]) / (self.__b.get()[0] - self.__a.get()[0]);
            b = -k * self.__a.get()[0] + self.__a.get()[1];

            if (pt.get()[1] == k * pt.get()[0] + b):
                return True;
            else:
                return False;

    def on_segment(self, pt):
        left_x = min([self.__a.get()[0], self.__b.get()[0]]);
        right_x = max([self.__a.get()[0], self.__b.get()[0]]);

        # y check for vertical lines

        low_y = min([self.__a.get()[1], self.__b.get()[1]]);
        upp_y = max([self.__a.get()[1], self.__b.get()[1]]);

        if (self.on_line(pt) and pt.get()[0] >= left_x and pt.get()[0] <= right_x and pt.get()[1] >= low_y and pt.get()[1] <= upp_y):
            return True;
        else:
            return False;

    def area(self, pt):
        return 0.5 * abs(pt.get()[0] * (self.__a.get()[1] - self.__b.get()[1]) + self.__a.get()[0] * (self.__b.get()[1] - pt.get()[1]) + self.__b.get()[0] * (pt.get()[1] - self.__a.get()[1]));


