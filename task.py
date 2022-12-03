# 1. Напишите программу, 
# которая принимает на вход вещественное число и показывает сумму его цифр

# num = input("Введите число: ")
# sum = 0
# for i in num:
#     if i.isdigit():
#         sum += int(i)
#         print(sum)

# 2. Задайте список из n чисел последовательности (1 + 1/n)^n.
# Вывестив консоль сам список и сумму его элементов.

# n = int(input('Введите число: ')) 

# def get_squerence(n):
#     return [round((1 + 1 / x)**x, 5) for x in range (1, n + 1)]

# nums = get_squerence(n)
# print(nums)
# print(round(sum(nums), 5))

# 3. Реализуйте алгоритм перемешивания списка.
# Встроенный алгоритм SHUFFLE не использовать! 

# import random
# list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,]
# print("Начальный список:  " + str(list))
# for i in range(len(list)-1, 0, -1):
#     j = random.randint(0, i + 1)
#     list[i], list[j] = list[j], list[i]
# print("Перемешанный список: " + str(list))    

# 1. Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка,стоящих на нечётной позиции.

# x = [2, 3, 6, 10, 12, 16, 5]
# summ = 0
# for i in range(1, len(x), 2):
#     if i % 2 == 1:
#         summ += x[i]       
# print(f"{x} -> сумма элементов на нечётных позициях: {summ}")   

# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# from random import randint
# number = int(input("Введите размер списка "))
# list = []
# list2 = []

# for i in range(number):
#     list.append(randint(0, 9))

# for i in range(len(list)):
#     while i < len(list)/2 and number > len(list)/2:
#         number = number - 1
#         a = list[i] * list[number]
#         list2.append(a)
#         i += 1

# print(list)
# print(list2)

# 3. Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением
# дробной части элементов.

# from random import uniform
# n = int(input('Введите размер списка '))
# list1 = []
# for i in range(n):
#     f = uniform(0, 9)
#     list1.append(round(f, 2))
# min = list1[0]
# max = 0
# for i in range(len(list1)):
    #     if max < list1[i]:
#         max = list1[i]
#     if min > list1[i]:
#         min = list1[i]
# dif = (max - int(max)) - (min - int(min))
# print(list1)
# print(max, min)
# print(round(dif,2))

# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.


# s = ""
# n = int(input("Введите число для преобразовывания десятичного числа в двоичное:\n"))
# while n != 0:
#     s = str(n%2) + s
#     n //=2
# print(s)

# 5. Задайте число. Составьте список чисел Фибоначчи,
# в том числе для отрицательных индексов (Негафибоначчи).

# n = int(input('Введите число: '))
# def get_fibonacci(n):
#     fibo_nums = []
#     a, b = 1, 1
#     for i in range(n-1):
#         fibo_nums.append(a)
#         a, b = b, a + b
#     a, b = 0, 1
#     for i in range (n):
#         fibo_nums.insert(0, a)
#         a, b = b, a - b
#     return fibo_nums
# fibo_nums = get_fibonacci(n)
# print(get_fibonacci(n))
# print(fibo_nums.index(0))