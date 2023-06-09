# 10.7

from mod import *

d1 = input_date();
d2 = input_date();

flg = 1;

if (is_less(d2, d1)):
    tmp = d1;
    d1 = d2;
    d2 = tmp;
    flg = -1;


days = 0;

while (is_less(d1, d2)):
    d1 = next_day(d1);
    days = days + 1;

result = 0 if days == 0 else (flg * (days - 1));

print(f"Result: {result} day(s) between");
