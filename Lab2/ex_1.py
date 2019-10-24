#!/usr/bin/env python3
from librip.gens import *

goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'},
    {'title': 'Стелаж', 'price': 7000, 'color': 'white'},
    {'title': 'Вешалка для одежды', 'price': 800, 'color': 'white'}
]


# Реализация задания 1

a = field(goods, 'title')
b = field(goods, 'title', 'price')
arr = gen_random(1, 3, 5)

print(list(a))
print(list(b))
print(list(arr))


print(list(a))

