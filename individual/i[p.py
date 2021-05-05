#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

if __name__ == '__main__':
    n = int(input("Введите число: "))
    r = []

    if n >= 1000:
        print('Число больше 1000')

    h = ["сто", "двести", "триста", "четыреста", "пятьсот", "шестьсот", "семьсот", "восемьсот", "девятьсот"]
    o = ["один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]
    s = ["одиннадцать", "двенадцать", "тринадцать", "четырнадцать", "пятнадцать", "шестнадцать", "семьнадцать",
         "восемнадцать", "девятнадцать"]
    t = ["десять", "двадцать", "тридцать", "сорок", "пятьдесят", "шестьдесят", "семьдесят", "восемьдясят", "девяносто"]

    if n == 1000:
        print('Тысяча')
        exit(1)

    if n // 100 > 0:
        x = n // 100
        r.append(h[x - 1])

        if (n % 100) // 10 >= 2:
            x = (n % 100) // 10
            r.append(t[x - 1])

            if (n % 100) % 10 != 0:
                x = (n % 100) % 10
                r.append(o[x - 1])
                r = " ".join(r)
                print(r)
                exit(1)


    if 11 <= n % 100 < 20:
        x = (n % 100) % 10
        r.append(s[x - 1])
        r = " ".join(r)
        print(r)
        exit(1)

    if n % 100 // 10:
        x = n % 100 // 10
        r.append(t[x - 1])

    if n % 10 > 0:
        x = (n % 10)
        r.append(o[x - 1])

    r = " ".join(r)
    print(r)
