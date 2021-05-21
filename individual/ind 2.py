#!/usr/bin/env python3
import math
import sys



# Проверяет, является ли числом
def isDigit(x):
    try:
        float(x)
        return True
    except ValueError:
        return False


if __name__ == '__main__':

    print("Введите элементы вещественного типа в массив через пробел:")
    a = tuple(map(float, input().split()))
    # Копии списка для замены элементов путём удаления и создания кортежей
    b = a
    c = a
    # Количество отрицательных чисел
    negative = 0
    # Сумма модулей после минимального элемента(по модулю)
    summ = 0
    # Минимальный элемент
    a_min = a[0]
    i_min = 0

    # Проходит по всем элементам массива
    for i, item in enumerate(a):

        if not isDigit(a[i]):
            print("Не все элементы массива являются числами", file=sys.stderr)
            exit(1)

        # Считает отрицательные элементы и возводит их в квадрат
        if a[i] < 0:
            del c
            c = b + (a[i]**2,)
            del b
            b = c
            negative += 1

        # Ищет минимальный элемент
        if math.fabs(item) < a_min:
            i_min, a_min = i, math.fabs(item)

    # Проходит по элементам после минимального, считает их сумму и возводит в квадрат
    # оставшиеся элементы
    for i in enumerate(a, start=i_min):
        summ += math.fabs(i[1])

    # Сортирует по возрастанию
    b = tuple(sorted(c))
    # Стирает лишние отрицательные элементы(в начале)
    del c
    c = b[negative:]

    print(f"\nКоличество отрицательных элементов кортежа: {negative}")
    print(f"\nСумма модулей элементов кортежа, расположенных после минимального по модулю")
    print(f"элемента: {summ}")
    print(f"\nВсе отрицательные элементы кортежа были заменены их квадратами,")
    print(f"а затем, кортеж был упорядочен по возрастанию:\n{c}")
