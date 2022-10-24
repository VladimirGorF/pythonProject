# задача 2 . Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов
# исходной последовательности.
listS = [8, 8, 12, 14, 4, 1, 5, 6, 8, 4]
listIndex = []
listN = []

def find_Index():
    for i in range(len(listS)):
        for j in range(i+1, len(listS)):
            if listS[i] == listS[j]:
                if i not in listIndex:
                    listIndex.append(i)
                if j not in listIndex:
                    listIndex.append(j)


def filterR():
    for i in range(len(listS)):
        if i not in listIndex:
            listN.append(listS[i])
    return listN


find_Index()

print(filterR())

