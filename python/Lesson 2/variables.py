string = "Это строка" # Тип str
intager = 8 # Тип int

print(string)
# Вывод: Это строка


print(intager)
# Вывод: 8


# Есть другой способ присваивания
name, age = "Mark", 26 # Он обычно не используется, но нужен для понимания следующей конструкции
print(name, age)
# Вывод: Mark 26


# Обмен двух переменных значениями
name, age = age, name
print(name, age)
# Вывод: 26 Mark