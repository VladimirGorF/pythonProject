# задача 3. Задана натуральная степень k. Сформировать случайным образом список
# # коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k. *Пример:*
# #
# # - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

def create_Coefficients(k):
    coefficients = [randint(0, 100) for i in range(k + 1)]
    while coefficients[0] == 0:
        coefficients[0] = randint(0, 100)
    return coefficients

def create_Polynom(k, coefficients):
    var = ['*x^']*(k-1) + ['*x']
    polynom = [[a, b, c] for a, b, c in itertools.zip_longest(coefficients, var, range(k, 1, -1), fillvalue='') if a != 0]
    for x in polynom:
        x.append(' + ')
    polynom = list(itertools.chain(*polynom))
    polynom[-1] = ' = 0'
    return "".join(map(str, polynom)).replace(' 1*x', ' x')


try:
    from random import randint
    import itertools

    k = randint(2, 15)

    coefficients = create_Coefficients(k)
    polynom1 = create_Polynom(k, coefficients)

    with open('Polynom.txt', 'a') as data:
        data.write(polynom1)

    k = randint(2, 15)

    coefficients = create_Coefficients(k)
    polynom2 = create_Polynom(k, coefficients)

    with open('Polynom2.txt', 'a') as data:
        data.write(polynom2)
except:
    print('Please be careful!')
