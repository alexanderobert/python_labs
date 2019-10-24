#!/usr/bin/env python3
from librip.gens import gen_random
from librip.iterators import *

data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
data2 = gen_random(1, 3, 10)
data3 = [1,1,2,3,3,3,4,'F','f','a','b','B']

# Реализация задания 2
a = Unique(data1)
b = Unique(data2)
c = Unique(data3)
c1 = Unique(data3, 1)
print(list(a))
print(list(b))
print(list(c))
print(list(c1))
