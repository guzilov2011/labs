#!/usr/bin/env python3
from librip.gen import gen_random
from librip.iterators import Unique

data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
data2 = gen_random(1, 4, 8)
data3 = ['a', 'A', 'b', 'c', 'B', 'C']
# Реализация задания 2
print (list(Unique(data1))) #Unique(data) будет последовательно возвращать только 1 и 2
print (list(Unique(data2))) #Unique(gen_random(1, 3, 10)) будет последовательно возвращать только 1, 2, 3 и 4
print (list(Unique(data3, ignore_case=True))) #Unique(data, ignore_case=True) будет последовательно возвращать только a, b, c
