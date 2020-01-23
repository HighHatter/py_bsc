a = ''
b = ''
while not a.isdigit():
    while not b.isdigit():
        a = input('Введите целую нижнюю границу промежутка: ')
        b = input('Введите целую верхнюю границу промежутка: ')
x = int(a)
y = int(b)
print('Сумма чисел на промежутке равна: ', ((x+y)/2)*(y-x+1))
