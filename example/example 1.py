import sys

# Ввести кортеж одной строкой
A = tuple(map(int, input().split()))
# Проверить количество элементов кортежа
if len(A) != 10:
    print("Неверный размер кортежа", file=sys.stderr)
    exit(1)

# Найти искомую сумму
s = sum(a for a in A if abs(a) < 5)

print(s)