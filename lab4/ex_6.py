#!/usr/bin/env python3
import json
import sys
import random
from librip.ctxmngrs import timer
from librip.decorators import print_result
from librip.gen import field, gen_random
from librip.iterators import Unique as unique

path = r"F:\РИП\лаба4\untitled1\data.json"

# Здесь необходимо в переменную path получить
# путь до файла, который был передан при запуске

with open(path, encoding="utf-8") as f:
 data =json.load(f)


# Далее необходимо реализовать все функции по заданию, заменив `raise NotImplemented`
# Важно!
# Функции с 1 по 3 дожны быть реализованы в одну строку
# В реализации функции 4 может быть до 3 строк
# При этом строки должны быть не длиннее 80 символов

@print_result
def f1(arg):
   return sorted(unique(field(arg, 'job-name'), ignore_case=True), key= lambda x: x.lower())
@print_result
def f2(arg):
    return ([prof for prof in arg if "программист" in prof])
@print_result
def f3(arg):
    return ([prof+" с опытом Python" for prof in arg])
@print_result
def f4(arg):
	rand= lambda : random.randint(100000,200000)
	return([prof+", зарплата "+str(rand())+"руб" for prof in arg])
with timer():
	f4(f3(f2(f1(data))))

