f1 = 1
f2 = 1
print('Ряд чисел Фибоначчи всегда начинается с', f1, ',', f2)
n = int(input('Введите сколько чисел Фибоначчи вывести на экран: '))
if n < 2:
    quit()

print(f1, end=' ')
print(f2, end=' ')
for i in range(2, n):
    f1, f2 = f2, f1 + f2
    print(f2, end=' ')
