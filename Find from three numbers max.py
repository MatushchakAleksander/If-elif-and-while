"""Пользователь вводит с клавиатуры три числа в переменные a, b, c.
Найдите наибольшее число из них и запишите в переменную max."""

 
a = int(input('Enter the first number: '))
b = int(input('Enter the second number: '))
c = int(input('Enter the third number: '))
max = 0

if  b <= a >= c:
    max = a 
    
if  a <= b >= c:
    max = b 
     
elif a <= c >= b:
     max = c    
   
print("The max is: ",MAX) 
    




#Оптимальный вариант решения:
#print(max(a,b,c))


