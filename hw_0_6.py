a=float(input('Input side A: '))
b=float(input('Input side B: '))
c=float(input('Input side C: '))
p=(a+b+b)/2
print('Half perimetr equals: ', p)
S=sqrt(p*(p-a)*(p-b)*(p-c))
print('The area of triangle equals: ', S)