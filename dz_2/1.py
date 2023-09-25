# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление. 
# Функцию hex используйте для проверки своего результата.

num = int(input("Ведите число: "))
hex_values = "0123456789abcdef"
hex_resalt = ""
while num > 0:
    hex_resalt = hex_values[num % 16] + hex_resalt
    num = num // 16
print(f"Шестнадцатеричное представление числа = {hex_resalt}")

# Проверка
number = 125
print(number, 'in hex =', hex(number))