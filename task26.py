# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
#
# *Пример:*
#
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8

a = int(input("enter a: "))
b = int(input("enter b: "))
def pow(a, b):
    if b == 0:
        return 1
    if b == 1:
        return a
    return pow(a, b-1) * a
print(pow(a, b))