"""Пользователь вводит с клавиатуры три числа в переменные a, b, c.
Если все числа больше 10 и первые два числа делятся на 3,
то вывести yes, иначе no."""


a = int(input('Enter the first number: '))
b = int(input('Enter the second number: '))
c = int(input('Enter the third number: '))

if a>10 and b>10 and c>10 and  a%3 == 0 and b%3 ==0:
    print('Yes')
    
else:
    print('No')
