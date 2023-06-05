# 18.11

class CompareMixin:

    def __eq__(self, comp):         # self == comp
        
        return ( ( not (self < comp) ) and ( not (comp < self) ) );

    def __ne__(self, comp):         # self != comp
        return not (self == comp);

    def __le__(self, comp):         # self <= comp
        return not (comp < self);

    def __gt__(self, comp):         # self > comp
        return (comp < self);

    def __ge__(self, comp):         # self >= comp
        return not (self < comp);

class WeightedList(list):

    def weight(self):

        res = 0;

        for i in self:
            res = res + abs(i);

        return res;

    def __lt__(self, comp):
        return ( self.weight() < comp.weight() );

class FullOrderWeightedList(CompareMixin, WeightedList):
   
    pass;

condition = True;

lst = [];

while (condition):
    num = int(input("1. add list\n2. end\nEnter number: "));
    if (num == 1):
        n = int(input("Enter number of elements: "));
        tlst = [];
        for i in range(1, n + 1):
            tlst = tlst + [float(input(f"Enter {i} element: "))];

        lst = lst + [tlst];
    elif (num == 2):
        condition = False;
    else:
        print("Wrong number");

lst = list(map(FullOrderWeightedList, lst));

res = True;
prev = lst[0];
lst = lst[1:];

for elem in lst:
    if (elem != prev):
        res = False;
        break;
    prev = elem;

print(f"Result: {res}");
