# даны действительный числа x и y
# x=int (input("Ведите число:"))
# y= int (input("Введите чиисло:"))
# print(abs(x)-abs(y)/1+ abs(x*y))

# 2.		Даны катеты прямоугольного треугольника. Найти его гипотенузу и площадь
# import math
# x=int (input("Ведите число:"))
# y= int (input("Введите чиисло:"))
# c= math.sqrt(x**2+y**2)          # квадрат гиппотенузы равен сумме квадратов катетов
# print(c)
# S= (x+y)/2
# print(S)

# 3
# a=9
# b=17
# c=5
# if a>b:
#     print("True",a>b)
# elif a!=b-c:
#     print("True",a,"!=", (b-c))
# elif b==a+c:
#     print("True")
# print(c<=a+b)
# print(a<b and a>c)
# print(b>a or b>c)

# 4	Перевести строку в массив по пробелу "Robin Singh" => ["Robin”, “Singh"]

# a ="Robin Singh"
# print(a.split(" "))

# "I love arrays they are my favorite" => ["I", "love", "lists", "they", "are", "my", "favorite"]

# b="I love arrays they are my favorite"
# b1=b.replace("arrays","list")
# print(b1.split(" "))


# 5	Дан список ["I", "love", "lists", "they", "are", "my", "favorite"] сделайте из него строку => "I love arrays they are my favorite"


# a=["I", "love", "lists", "they", "are", "my", "favorite"]
# a[2]= "arrays"
# print(" ".join(a))

# Даны несколько списков: [-8, 1, 2, -2, 0], [1, -1, 0, -9, 4, -5], [1, 4, 0, 23, 6, 34].
# Для каждого из списков найти второе наименьшее значение в нем (правильные ответы выделены жирным шрифтом).

# a= [-8, 1, 2, -2, 0]
# b=[1, -1, 0, -9, 4, -5]
# c=[1, 4, 0, 23, 6, 34]
# a.sort()
# b.sort()
# c.sort()
# print(a[1],b[1],c[1])

# 7Дан #7 список цветов: ‘red’, ‘green’, ‘white’, ‘black’, ‘pink’, ‘yellow’.
# Создайте еще один список и переместите в него 1-ый, 5-ый и 6-ой элементы.

# a= ["red","green","white","black","pink","yellow"]
# b=[]
# b.append(a[0])
# b.append(a[4])
# b.append(a[5])
# print(b)

# 8.	Даны два целых числа m и n (m≤n). Напишите программу, которая  выводит все числа от m до n включительно.
# m= int(input("введите целое число:"))
# n= int(input("введите второе число, которое больше или равно первого"))
#
# for i in range(m,n+1):
#   print(i)

# 9.	 Даны два целых числа m и n.
# Напишите программу, которая выводит все числа от m до n включительно в порядке возрастания,если m<n,
# или в порядке убывания в противном случае.
#
# m= int(input("введите целое число:"))
# n= int(input("введите второе целое число:"))
#
# for i in range(m,n+1):
#       if m<n:
#        print(i)
# for i in range(m,n-1,-1):
#       if m>n:
#          print(i)

# 10.С помощью цикла while просите пользователя решить пример, пока он не введет правильный ответ.
# Так же у пользователя есть заданное количество попыток. Если он их использовал, то вывести об этом сообщение
# print("решите задачу: 4+4-2=")
# n = 3    # попытки
# answ = 6    #ответ
# print("у Вас", n, "попыток")
# answ1 = int(input("Введите ответ:"))
# while n > 0:
#     n -= 1
#     if answ1 != answ:
#         print("не верно")
#         print("осталось ", n, "попытки")
#     if n == 0:
#         print("вы использовали все попытки")
#         break
#     answ1=int(input("Введите ответ еще раз:"))
# if n>0:
# print("верно")




