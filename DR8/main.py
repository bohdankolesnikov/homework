# 14.10

from mod import *
import random

def test0(deque):
    print("test #0");
    print(deque.pop_front());

def test1(deque):
    print("test #1");
    deque.push_front(float(input("Enter value: ")));

def test2(deque):
    print("test #2");
    print(deque.pop_back());

def test3(deque):
    print("test #3");
    deque.push_back(float(input("Enter value: ")));


seq = list(map(float, input("Enter sequence for stack separated by comma: ").replace(" ", "").split(",")));

# stack 14.8

stack = Stack();

# fill stack

for elem in seq:
    stack.push(elem);

#

seq = [];

while (not stack.is_empty()):
    seq = seq + [stack.pop()];

print(f"stack: {seq}");

# deque 14.8

seq = list(map(float, input("Enter sequence for deque separated by comma: ").replace(" ", "").split(",")));

deque = Deque();

# fill deque

for elem in seq:
    deque.push_back(elem);

#

func_lst = [test0, test1, test2, test3];

func_lst[random.randrange(0, 3)](deque);

seq = [];

while (not deque.is_empty()):
    seq = seq + [deque.pop_back()];

print(f"deque: {seq}");


