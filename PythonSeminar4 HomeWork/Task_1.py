# задача 1. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def Multiplier(Z):
    k = 2
    for i in range(2, 100000):
        if Z % k == 0:
            Multipliers_List.append(k)
            Z /= k
        else:
            k += 1


n = int(input('Please input N '))
Multipliers_List = []
Multiplier(n)
print(Multipliers_List)


