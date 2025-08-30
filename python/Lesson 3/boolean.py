right = True
lie = False

print(right, lie)
# Вывод: True False

number1 = 23
number2 = 23

print(number1 == number2) # Проверка на равенство (Дав ровно потому-что 1 это просвоение значения)
# Вывод: True 

print(number1 != number2) # Проверка на неравенство 
# Вывод: False

number1 = 12
number2 = 13

print(number1 == number2)
# Вывод: False

isEqual = number1 == number2
print(isEqual)
# Вывод: False

number1 = 34
number2 = 34

print(number1 >= number2) # Больше или равно
# Вывод: True

print(number1 <= number2) # Меньше или равно или равно
# Вывод: True

print(number1 > number2) # Больше 
# Вывод: False

print(number1 < number2) # Меньше 
# Вывод: False


number1 = 1
print(number1 < 5 and number1 > -2)  # Логическое и (верны обе части выражения)
# Вывод: True

number1 = 6
print(number1 < 5 and number1 > -2)
# Вывод: False


number1 = 1
print(number1 < 5 or number1 > -2)  # Логическое или (верна хотябы 1 часть)
# Вывод: True

number1 = 6
print(number1 < 5 or number1 > -2)
# Вывод: True


right = True
print(not right)  
# Вывод: False

print(bool(1))
# Вывод: True
  
print(bool(0))
# Вывод: False

print(bool(-1))
# Вывод: True 


print(bool("Привет. Мир!")) # Не пустое и не равно 0
# Вывод: True

print(bool("")) # Пустое выражение
# Вывод: False


print(int(True))
# Вывод: 1

print(int(False))
# Вывод: 0