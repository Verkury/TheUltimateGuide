number1 = 10
number2 = 5
summary = number1 + number2
print(summary)  
# Вывод: 15

number1 = 10.5
number2 = 5.5
summary = number1 + number2
print(summary)  
# Вывод: 16.0

number1 = 10
number2 = 5
number3 = number1 * number2
print(number3)  
# Вывод: 50

number1 = 10
number2 = 5
number3 = number1 / number2 # Деление
print(number3)  
# Вывод: 2.0

number1 = 10
number2 = 0
# number3 = number1 / number2 # Ошибка деление на ноль
# print(number3)  
# Вывод: ZeroDivisionError: division by zero

firstInteger = 10
secondInteger = 5
summary = firstInteger + secondInteger
print(summary)


number1 = 2
print(number1 ** 3) # Возвидене в степень
# Вывод: 8


number1 = 9
number2 = 4
print(number1 // number2) # Деление с округелением (округлене не всегда верно)
# Вывод: 2
print(number1 % number2) # Остаток от деления 
# Вывод: 1


integer = 2 + 3 * 5
print(integer)  
# Вывод: 17


integer = (2 + 3) * 5
print(integer)  
# Вывод: 25


myInteger = 10
myFloat = 5.5
print(myInteger + myFloat)  
# Вывод: 15.5


bigNumber = 10 ** 1000
print(bigNumber)  
# Вывод: Ооооочень большое число


myInt = 1
myFloat = float(myInt)
print(myFloat)  
# Вывод: 1.0


myFloat = 1.9999
myInt = int(myFloat)
print(myInt)  
# Вывод: 1


myFloat = 1.9999
myInt = round(myFloat) # Функция для точного округления 
print(myInt)  
# Вывод: 2