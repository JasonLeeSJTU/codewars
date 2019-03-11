#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: digital_root.py

@time: 2019/3/11 21:34

@desc:
A digital root is the recursive sum of all the digits in a number.
Given n, take the sum of the digits of n. If that value has more than
one digit, continue reducing in this way until a single-digit number
is produced. This is only applicable to the natural numbers.

Here's how it works:

digital_root(16)
=> 1 + 6
=> 7

digital_root(942)
=> 9 + 4 + 2
=> 15 ...
=> 1 + 5
=> 6
'''

# Good answer

def digital_root(n):
    return n if n < 10 else digital_root(sum(map(int,str(n))))

# My codes
def my_digital_root(n):
    temp = 0
    while len(str(n)) > 1:
        a = n % 10
        temp += a
        n = n // 10

    temp += n

    if len(str(temp)) > 1:
        temp = digital_root(temp)

    return temp


if __name__ == '__main__':
    test = digital_root(493193)
    print(test)