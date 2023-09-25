# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. 
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.


num_1_str = "2/8"
num_2_str = "3/5"

num_1, denominator_1  = map(int, num_1_str.split("/"))
num_2, denominator_2 = map(int, num_2_str.split("/"))

sum_fractional_num = num_1 * denominator_2 + num_2 * denominator_1 
sum_fractional_denom = denominator_1  * denominator_2
sum_fractional = (sum_fractional_num, sum_fractional_denom)
print(f"Сумма дробей {num_1_str} и {num_2_str} = {sum_fractional[0]}/{sum_fractional[1]}")

prod_fractional_num = num_1 * num_2
prod_fractional_denom = denominator_1  * denominator_2
prod_fractional = (prod_fractional_num, prod_fractional_denom)
print(f"Произведение дробей {num_1_str} и {num_2_str} = {prod_fractional[0]}/{prod_fractional[1]}")
