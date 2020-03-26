# Задачи на циклы и оператор условия------
# ----------------------------------------

'''
Задача 1
Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.
'''
# for i in range(1,6,1):
#     print(i,"00000")
'''
Задача 2
Пользователь в цикле вводит 10 цифр. Найти количество введеных пользователем цифр 5.
'''
# number = int(input("Введите цифру "))
# digits_number = 5
# count = 0
# for i in range(10):
#     number = int(input("Введите цифру "))
#     if number == 5:
#         count+=1
# print(count)

'''
Задача 3
Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.
'''
# sum = 0
# for i in range(1,101):
#     sum+=i
# print(sum)

'''
Задача 4
Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.
'''
# mult = 1
# for i in range(1,11):
#     mult*=i
# print(mult)
'''
Задача 5
Вывести цифры числа на каждой строчке.
'''
# integer_number = 15698
# while integer_number>0:
#     print(integer_number%10)
#     integer_number = integer_number//10

'''
Задача 6
Найти сумму цифр числа.
'''
# n = int(input("Введите целое число:"))
# summa = 0
# while n > 0:
#     if n % 10 != 0:
#         summa = summa + n % 10
#     n = n // 10
# print("Сумма цифр:", summa)

'''
Задача 7
Найти произведение цифр числа.
'''
# n = int(input("Введите целое число:"))
# mult = 1
# while n > 0:
#     if n % 10 != 0:
#         mult = mult * (n % 10)
#     n = n // 10
# print("Произведение значащих цифр:", mult)
'''
Задача 8
Дать ответ на вопрос: есть ли среди цифр числа 5?
'''
# integer_number = 1555
# while integer_number > 0:
#     if integer_number % 10 == 5:
#         print('Yes')
#         break
#     integer_number = integer_number // 10
# else:
#     print('No')

'''
Задача 9
Найти максимальную цифру в числе
'''
# number = 142554987
# max_digit = 0
# while number > 0:
#     if number % 10 > max_digit:
#         max_digit = number % 10
#     number = number // 10
# print(max_digit)

'''
Задача 10
Найти количество цифр 5 в числе
'''
# m = 142554987
# d = 5
# count = 0
# while m > 0:
#     if m % 10 == d:
#         count += 1
#     m = m // 10
# print("Было введено %d цифр %d" % (count, d))
