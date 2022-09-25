    #Функция – это блок кода, который начинается с ключевого слова def,
    # названия функции и двоеточия, пример:
# def a_function():
#     print("Hello world!")
# a_function()

          #Пустая функция
# def empty_function():
#     pass

      #Создайте функцию, которая будет считать сумму чисел в массиве.

# def s():
#     list=[1,2,3]               #вариант 1
#     print(sum(list))
# s()

# def s():
#     sum=0                       #вариант 2
#     for i in range(4):
#          sum+=i
#     print(i)
#     print(sum)
# s()

        #Передача аргументов функции


# def ad(a,b):
#     return a+b             #мы можем вызвать функцию путем передачи двух значений.
# print(ad(1,2))             # Если вы передали недостаточно, или слишком много аргументов для данной функции,
                             # вы получите ошибку.


# def ad(a,b):
#      print(a+b)        #3
# print(ad(1,2))         # None



    # def ad(a, b):
#     print(a + b)
#  ad(1, 2)                  #3



# def ad(a,b):
#      return a+b
# print(ad(a=2,b=3))          #5


# total=ad(b=4,a=5)
# print((total))             #9


#Параметр — это имя в списке параметров в первой строке определения функции.
# Он получает свое значение при вызове.  a и b - это параметры
                      # def ad(a,b):
                      #     return a+b
# Аргумент — это реальное значение или ссылка на него, переданное функции при вызове.

                     #print(ad(1, 2))   1 и 2 - это аргумент


                  #Ключевые аргументы
# def mixed_function(a, b=2,c=3):
#      return a+b+c
# mixed_function(b=4,c=5)   # не хватает инфы
# print(mixed_function(1,b=4,c=5))  # если нужно поменять значение ключевых параметров
# print(mixed_function(1))  # достаточно одного значения если ключевые

          #*args и **kwargs
# def many(*args,**kwargs):
#      print(args)             #Чтобы получитm бесконечное количество аргументов, мы используем    *args,
#      print(kwargs)           # чтобы получить бесконечное количество ключевых аргументов   -    **kwargs.
# many(1,2,3,name="Mike", job="programmer")
                            # # результат:
                            # # (1,2,3)
                            # #{name:"Mike", job:"programmer"}
#Функция показывает нам два типа аргументов. Как мы видим, параметр  args превращается в кортеж,
# а kwargs – в словарь.

       #Область видимость и глобальные переменные
# def function_a():
#      global a
#      a=1
#      b=2
#      return a+b
# def function_b ():
#      c=3
#      return a+c
# print(function_a())
# print(function_b())


      #Вложенная функция

# def func1(a,b):
#      def inner_func(x):
#           return x**3
#      def inner_func2(y):
#           return y**2
#      return inner_func(a)+inner_func2(b)
# print(func1(2,3))



     #запись в одно строчку
# def summa (a,b): return a+b
# print(summa(1,5))


         #Задача №2
#Написать функцию is_year_leap, принимающую 1 аргумент - год
# и возвращающую  True если год високосный и False иначе
#вариант 1
# def is_year_leap(year):
#      return year%4==0 and year%100!=0 or year%400==0
# print(is_year_leap(int (input("Введите год:"))))

#вариант 2

# def is_year_leap():
#      year=int (input("Введите год:"))
#      return year % 4 == 0 and year % 100 != 0 or year % 400 == 0
# print(is_year_leap())

#вариант 3
# def is_year_leap(year):
#      return year%4==0 and year%100!=0 or year%400==0
# print(is_year_leap(2022))


 #Задача №3
#Написать функцию square , принимающу. 1 аргумент -  сторону квадрата
# и возвращающая 3 значения ( с помощью кортежа): периметр квадрата, площадь, диагональ квадрата.
# сторону квадрата вводить с клавиатуры
# import math
# def square ():
#      side=int(input("Введите сторону квадрата:"))
#      p=side*4
#      sq=side**2
#      d=side*math.sqrt(2)
#      return p,sq,d   #через , выводит данные в вортеже
# print(square())


#Задача №4
#Написать функцию season, принимающую 1 аргумент — номер месяца (от 1 до 12),
# и возвращающую время года, которому этот месяц принадлежит (зима, весна, лето или осень).
# Номер месяца вводить с клавиатуры.

# def season(n):
#      if 1<=n<=2 or n==12:
#           print("Зима")
#      elif 3<=n<=5:
#           print("Весна")
#      elif 6<=n<=8:
#           print("Лето")
#      elif 9<=n<=11:
#           print("Осень")
#      else:
#           print("вы ввели недопустимое число")
# season(int (input("Введите число месяца:")))


#Задача5
#Написать функцию is_prime, принимающую 1 аргумент — число от 0 до 1000,
# и возвращающую True, если оно простое, и False - иначе.
# def is_prime(n):
#     d=2
#     while n%d!=0:
#         d+=1
#     return  d==n
# n=int(input("Введите число"))
# print(is_prime(n))


#задача 6
#Функция, вычисляющая среднее арифметическое элементов массива.
# Массив должен состоять из случайных чисел, длинной 10 элементов
# import random
#
# mass=[random.randint(1,100) for i in range (10)]
# def average(mass):
#     s=sum(mass)
#     return s/10
# print(mass)
# print(average(mass))

print("hellow")