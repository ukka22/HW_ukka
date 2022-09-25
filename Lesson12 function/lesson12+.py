#Рекурсивная функция- которая вызывает сама себя.
# def factorial(n):
#     if n!=0:
#         return n*factorial(n-1)
#     else:
#         return 1
# print(factorial(5))                      #120

#Присвоение функции переменной
# def add(a,b):
#     return a+b
# variable=add(1,2)
# print(variable)

# Присвоение функции несколько значений
#Переменным также можно присваивать встроенные функции.
#Таким образом позже есть возможность вызывать функцию другим именем

# def func(x): return x
# a1=func
# a2=a1
# print(a2(10))     #Такой подход называется непрямым вызовом функции.


          #Анонимная функция лямбда ( без обьявления def)
# -это короткая однострочная функция, которой даже не нужно имя давать.
# Такие выражения содержат лишь одну инструкцию, поэтому, например, if, for и while использовать нельзя


# product=lambda x,y: x*y
# print(product(2,3))

#В отличие от функций, здесь не используется ключевое слово return.
# Результат работы и так возвращается.

# print(type (product))   #<class 'function'>

      #Функция внутри функции в Python
      
# def mul (a):     # -главная функция
#     def helper(b):    #- второстепенная  и обязательно вернуть
#         return a*b
#     return helper
# print(mul(3)(2))

                 # Декоратор функции

# def simple_decore(fn):
#     print("Start function")
#     fn()
#     print("Stop function")
# @simple_decore
# def first_test():
#     print("Hello Yulia")
# @simple_decore
# def first_test():
#     print("Hello Max")


         #Задача  №1
#Написать функцию, которая определяет количество разрядов введенного целого числа.

  #вариант1
# def count (n):
#     c=0
#     for i in str(n):
#         c+=1
#     return c
# print(count(int(input("Введите число"))))

#  #вариант2
# def count (n):
#     c=0
#     while n >0:
#         n=n//10
#         c+=1
#     return c
# print(count(int(input("Введите число"))))



       #Задача 2
#В зависимости от выбора пользователя вычислить площадь круга,
# прямоугольника или треугольника.
# Для вычисления площади каждой фигуры должна быть написана отдельная функция.
# функция
# import math
# def circle(r):
#     A=math.pi*r**2     #площадь круга A=рi * радиус в квадрате
#     return A
#
# def rectangle(a,b):
#     return a*b         #площадь прямоугольника
#
# def triangle(a,b,c):
#     p= (a+b+c)/2                  #полупериметр
#     s=math.sqrt(p*(p-a)*(p-b)*(p-c))
#     return  s
#
# tip= input("Введите название фигуры-")
# if tip== "круг":
#     r=float(input("Введите радиус r="))
#     print("площадь круга:%2f" % circle(r))
# elif tip== "прямоугольник":
#     a=float(input("Введите сторону a="))
#     b = float(input("Введите сторону b="))
#     print("площадь прямоугольника:%2f" % rectangle(a,b))
# elif tip== "треугольник":
#     a=float(input("Введите сторону a="))
#     b = float(input("Введите сторону b="))
#     c = float(input("Введите сторону с="))
#     print("площадь треугольника:%2f" % triangle(a,b,c))


                      #Задача №4
#Написать функцию и сделать так, чтобы число секунд отображалось
#в виде дни:часы:минуты:секунды
# def convert(sec):
#     day=sec//86400
#     sec=sec%8600
#     hours=sec//3600
#     sec%=3600
#     min=sec//60
#     sec%=60
#     print(f'{day}: {hours} : {min} : {sec}')       # print(day,":",hours,":",min,":",sec)
# convert(6789)


                       #Задача №5
#Написать функцию, которая считает сколько гласных и согласных в строке.
# Строку вводить с клавиатуры.
# def count (str):
#     A=0
#     B=0
#     for i in str:
#        if i.isalpha():
#            if i.lower() in "aeouiy":
#               A+=1
#            else:
#               B+=1
#     print("Гласных-", A, "\n", "Согласных-", B)
#
#
# count(input("Введите строку:"))




                      #Задача 6
#Функцию которая при  заданном  целом числе n посчитает n + nn + nnn.
                    # вариант 1
# def function (n):
#    n1=n
#    nn=int(str(n)*2)
#    nnn=int(str(n)*3)
#    sum=n1+nn+nnn
#    return sum
# print(function(2))
#

# #вариант 2
# def function (n):
#     return n+ (n*10+n)+(n*100+(n*10+n))
# print(function (1))


#  # попытка через рукурсивную функцию но нет !!!!!!!!!!!!!
# def function (N):
#
#     if len(str(N))<3:
#
#        summ =N+function(N*10)
#        return summ
#     else:
#        return 0
#
# print(function(1))


              #Задача 7
#Вычислить значения нижеприведенной функции в диапазоне значений x от -10 до 10 включительно с шагом, равным 1.
#y = 𝑥^2 при -5 <= x <= 5;
#y = 2*|x|-1 при x < -5;
#y = 2x при x > 5.
#Вычисление значения функции оформить в виде программной функции, которая принимает значение x, а возвращает полученное значение функции (y).
def function (x):
    if -5 <= x <= 5:
        return x**2
    elif x < -5:
        return x * abs(x)-1
    else:
        return x*2
for i in range (-10,11):
  print(function(i),end=" ")
print()
