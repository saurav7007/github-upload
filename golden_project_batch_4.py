# -*- coding: utf-8 -*-
"""Golden_Project_batch-4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VVe1FPpMHdcjGkmwQ9QQzozGZ9Pk8BhP

**Golden Project**
"""

import math

t = int(input("Please enter the total number of passengers.\n It should be from 1 to 105: "))
while 1 > t or 105 < t:
    print("Please input valid number")
    t = int(input())  # It breaks the loop

l1 = []

for item in range(0, t):
    item = int(input("Please enter your seat no.s of from 1 to 108: "))
    while 1 > item or 108 < item:
        print("Please input valid number")
        item = int(input())
    l1.append(item)

print("Your seat numbers are: ", l1)
l2 = l1.copy()

for i in l1:
    a1 = math.ceil(i / 6)
    if a1 % 2 != 0:
        a = list(range(6 * (a1 - 1) + 1, 6 * a1 + 1))
        b = list(range(6 * a1 + 1, 6 * (a1 + 1) + 1))
    else:
        a = list(range(6 * (a1 - 1) + 1, 6 * a1 + 1))
        b = list(range(6 * (a1 - 2) + 1, 6 * (a1 - 1) + 1))

    b.reverse()
    for x in a:
        if x == l2[0]:
            indexA = a.index(x)
            oppositeSeat = b[indexA]
            break
    if indexA == 0 or indexA == 5:
        print("The seat opposite to seat no. ", l2[0], " is ", oppositeSeat, " WS")
    elif indexA == 1 or indexA == 4:
        print("The seat opposite to seat no. ", l2[0], " is ", oppositeSeat, " MS")
    else:
        print("The seat opposite to seat no. ", l2[0], " is ", oppositeSeat, " AS")
    l2.pop(0)