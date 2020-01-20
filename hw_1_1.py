a = input('Please, input your first and second name: ')
print('Oh, hello ', a,)
b = int(input('Please, write your Birthday day: '))
c = int(input('Please, write your Birthday month: '))
d = int(input('Please, write your Birthday year: '))

acm = int(2020*12+1)#Months after Christ passed
acd = int(acm * 30 + 10)#Days after Christ passed

e = 2020 - d#years lived
f = e * 12 + 1#months lived
g = (30 - b) + ((c * 30)-1) + e * 365#days lived

print('You lived: ', e, 'years, and ', f, 'months')
print('Before beginning of this course you lived:', e, "years,", f, 'moths,', g, 'days')