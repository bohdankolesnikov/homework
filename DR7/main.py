# 13.23

from mod import *

sgmts = [];

'''

sge1 = SegmentEx(Point2(-2, 6), Point2(-4, 4));
sge2 = SegmentEx(Point2(0, 6), Point2(-2, 4));
sge3 = SegmentEx(Point2(5, 1), Point2(-4, 4));
sge4 = SegmentEx(Point2(3, 10), Point2(-1, -1));
sge5 = SegmentEx(Point2(-1, 0), Point2(0, 0));

sgmts = [sge1, sge2, sge3, sge4, sge5];


'''
flg = 1;

while (flg):
    x1, y1 = map(float, input("Enter first point (x,y) separated by comma: ").replace(" ", "").split(","));
    x2, y2 = map(float, input("Enter second point (x,y) separated by comma: ").replace(" ", "").split(","));

    sgmts.append(SegmentEx(Point2(x1, y1), Point2(x2, y2)));

    flg = int(input("1. add segment\n0. exit\nEnter number: "));


print(list(map(SegmentEx.__str__, sorted(sgmts))));
