
#1. Создать произвольный список
#2. Добавить новый элемент типа str в конец списка
#3. Добавить новый элемент типа int на место с индексом 5
#4. Добавить новый элемент типа list в конец списка
#5. Получить элемент по индексу
#6. Удалить элемент
#7. Найти число повторений элемента списка

# a= ["red", 67, "green",5, "white","black",678]
# n="pink"
# a.append(n)
# a[5]=78                #['red', 67, 'green', 5, 'white', 78, 678, 'pink']
# l=[4,"none",9]         #['red', 67, 'green', 5, 'white', 78, 678, 'pink', [4, 'none', 9]]
# a.append(l)
# print(a)
# print(a[2])            #green
# a.remove(67)           #['red', 'green', 5, 'white', 78, 678, 'pink', [4, 'none', 9]]
# print(a)
# print(a.count("green"))  #1

#Задача 1.2
#Получите первый и последний элемент списка

# a= ["red", 67, "green",5, "white","black",678]
# print(a[0],a[-1])

#Задача 1.3
#Поменяйте значения переменных a и b местами
  # вариант1
# a="Вася"
# b=78
# a,b=b,a
# print("a-",a,"b-",b)
  #вариант2
# a="Вася"
# b=78
# c=a
# a=b
# b=c
# print("a-",a,"b-",b)


#

#Задача1.4
#Создайте список[18, 14, 10, 6, 2]с помощью функции range()


# l=list(range(2,19))
# print(l[::-4])



#Задача 1.5
#Дана следующая строка: ‘Сидел барсук в своей норе и ел картошечку пюре’

#1.Создайте данную строку
#2.Получите ее длину
#3.Проведите операцию сложения со строкой ‘.’
#4.Проверьте, входит ли подстрока ‘ре’ в заданнуюстроку
#5.Посчитайте количество вхождений подстроки ‘ре’
#6.Получите предпоследний символ строки
#7.Получите все символы с нечетными индексами
# #8.Определите, сколько слов в строке
str= "Сидел барсук в своей норе и ел картошечку пюре"
# print(str)
# l=len(str)
# print(l)
# str1="."
# str2=str+str1
# print(str2)
# print("ре" in str)
# print(str.count("ре"))
# print(str[-2])
# print(str[1::2])
# print(len(str.split(" ")))

#Задача 1.6
#Сложите цифры пятизначного целого числа.

     #вариант 1
# import random
#
# a=random.randint(10000,100000)
# print(a)
# b=str(a)
# sum=0
# for i in b:
#     sum+=int(i)
# print(sum)

    #Вариант2
# import random
#
# a=random.randint(10000,100000)
# print(a)
# s=[int(i) for i in str(a)]
# print(s)
# print(sum(s))

#Задача 1.7
#Дана строка из двух слов. Поменяйте слова местами.
# a="Вася Иванов"
# print(a)
# a=a.split(" ")
#
# b=[a[-1],a[0]]
# b=" ".join(b)
# print(b)



#Задача 1.8
#Напишите программу, которая показывает приведенный ниже текст:
# Кошка сказала "мяу".
# text='Кошка сказала "мяу"'
# print(text)



#Задача 1.9
#С клавиатуры вводится десятизначное число.
# Вывести на экран четные числа входящие в данное число.
# Например 1234567892  2 4 6 7 8 2
# a = int(input("Введите десятизначное число:"))
# print(a)
# n=[int(i) for i in str (a)]
# print(n)
# for i in n:
#    if i%2==0:
#     print(i,end=",")

#Задача 1.10
#С клавиатуры вводится число. Необходимо перевернуть число.
# Например если ввели 1234 -> 4321
# a= int(input("Введите число:"))
# b=str(a)
# print(b)
# c=b[::-1]
# print(c)


#Задача 1.11
#В классе N школьников. На уроке физкультуры тренер говорит «на первый-второй рассчитайтесь».
# Выведите, что скажут ученики.
#Входные данные: Вводится одно целое число — количество человек в классе.
#Входные данные: Выведите последовательность чисел 1 и 2, в том порядке, как будут говорить школьники.
# stud=int(input("Колтчество человек в классе:"))
# i=1
# while i<=stud:
#     if i%2!=0:
#         print("Первый")
#     else:
#         print("Второй")
#     i+=1

#Задача 1.12
#С помощью срезов необходимо вывести:
#- весь список;
# a=["red", 67, "green",5, "pink",213, "white","black",678]
# print(a[::])
#
# #- нечётные по порядку элементы;
# print(a[::2])
# #- чётные по порядку элементы;
# print(a[1::2])
# #- все элементы в обратном порядке;
# print(a[::-1])
# #- все элементы, начиная с шестого;
# print(a[5:])
# #- все элементы, не доходя до шестого;
# print(a[:5])
# #- все элементы от предпоследнего до третьего в обратном порядке.
# print(a[-2:2:-1])


#Задача 1.13
#Необходимо удалить пустые строки из списка строк.
       #Вариант1
# a=["Необходимо", "", "удалить","", "пустые", "", "строки", "из", "", "списка" ,"строк","."]
# A=("").join(a).split()
# print(A)
        #Вариант2
# a=["Необходимо", "", "удалить","", "пустые", "", "строки", "из", "", "списка" ,"строк","."]
# A=list(filter(None,a))        #Если передать в функцию filter() None в качетсве первого аргумента,то
# print(A)                      # возвращаемый интератор отфильтрует любе значение, которое посчитает "примерно ложным"
#                               # Phyton считант false все значения что имеют длину 0
#                               # затем помещаем в функцию list, что бы вывести список



#Задача 1.14
#Дан список чисел. Превратите его в список квадратов этих чисел
# import random
#
# a=list(random.randint(0,20) for i in range(7))
#
# print(a)
# A=[int(i)**2 for i in a]
# print(A)

#Задача 1.15
#Дан список чисел, необходимо удалить все вхождения числа 20 из него.
# import random
#
# a=list(random.randint(18,25) for i in range(15))
# print(a)
# A=[i for i in a if i!=20]
#
# print(A)