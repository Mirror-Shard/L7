#!/usr/bin/env python3
import sys


if __name__ == '__main__':
    # Ввести список одной строкой
    print("Введите 10 целочисленных элементов в массив через пробел:")
    a = tuple(map(int, input().split()))

    if len(a) != 10:
        print("Неверный размер списка", file=sys.stderr)
        exit(1)

    sum = 0
    q = 0

    for i in enumerate(a, 0):
        if i[1] % 2 == 0:
            sum += i[1]
            q += 1

    print(f"Сумма чётных элементов равна: {sum}, всего чётных элементов: {q}")
