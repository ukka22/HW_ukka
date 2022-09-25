#1.	Добавьте на свой рабочий стол папку, в ней создайте 3 текстовых файла:
# test_1.txt, test_2.txt, test_3.txt.
import os
# print("текущая директория:", os.getcwd())
# os.mkdir("folder")                        #создать пустой каталог (папку)
# os.chdir("folder")                                                  # изменение текущего каталого на "folder"
# print("текущая директория изменилась на folder:", os.getcwd())
# f1=open("task_1.txt","w")                   #создаем файлы в режиме запись
# f2=open("task_2.txt","w")
# f3=open("task_3.txt","w")

#Затем переименуйте файлы на: rename_1.txt, rename_2.txt, rename_3.txt.
import os
# os.rename("task_1.txt.","rename_1.txt")    # переименовываем
# os.rename("task_2.txt.","rename_2.txt")
# os.rename("task_3.txt.","rename_3.txt")

#После этого удалите созданную папку.

# import shutil
# shutil.rmtree("folder")         #Удаляет папку с вложениями !!!!! - не сработал ( удалил только папку)

# import os
# os.remove("rename_1.txt")        #удаляем файлы
# os.remove("rename_2.txt")
# os.remove("rename_3.txt")

# os.rmdir("folder")               # удаляем уже пустую папку

#Все операции выполнять с помощью встроенных функций библиотеки os.





#2.	Даны два кортежа: C_1 = (35, 78,21,37, 2,98, 6, 100, 231)
                    # C_2 = (45, 21,124,76,5,23,91,234)
#Необходимо определить:
# 1) Сумма элементов какого из кортежей больше и вывести соответствующее сообщение на экран (Сумма больше в кортеже - ..)
# 2) Вывести на экран порядковые номера минимальных и максимальных элементов этих кортежей.

# C_1 = (35, 78,21,37, 2,98, 6, 100, 231)
# C_2 = (45, 21,124,76,5,23,91,234)
# s1= sum(C_1)
# s2=sum(C_2)
# if s1>s2:
#     print("Сумма больше в кортеже -", C_1,"\n", "И равна -",s1 )
# else:
#     print("Сумма больше в кортеже -", C_2,"\n", "И равна -",s2 )
#
# print("порядковые номера мин. значений:", C_1.index(min(C_1)),"и",C_2.index(min(C_2)),
#       "\n","порядковые номера макс. значений:", C_1.index(max(C_1)),"и",C_2.index(max(C_2)))



#3.	Напишите программу, демонстрирующую работу try\except\finally.
# print("Заполните Ваши данные:")
#
# try:
#  Name= input("Введите ваше имя-")
#  Age=int(input("Ваш возраст:"))
# except ValueError:
#  print("Вы ввели неверные данные")
# else:
#  print("Привет,", Name)
# finally:
#     print("Спасибо, за участие")



#4.	Создайте 2 множества:
#
# import random
# A=set(random.randint(0,5) for i in range(10))
# B=set(random.randint(0,5) for i in range(10))
# print(A)
# print(B)
#
# #- Если они одинаковые: вывести что они равны
# if len(A)==len(B):
#     print("Множества равны")
# #- Если 1 множество полностью состоит из второго: вывести сообщение множество 1
# #состоит из множества2
# if A>=B:                   # A.issuperset(B) -----> (True)
#     print("множество ",A, "состоит из множества", B)
#
# #- Если 2 множество полностью состоит из
# # 1: вывести сообщение множество 2 состоит из множества 1
# elif A.issubset(B):          # A<=B
#     print("множество ",B, "состоит из множества", A)
#
# #- Если они пересекаются: вывести элементы в которых они пересекаются
# if A&B:
#     print("Множества пересекаются по следующим элементам:",A&B)
#
# #- Если не пересекаются: вывести сообщение об этом
# else:
#     print("Множества не пересекаются")





#5.	Создайте словарь из строки ' An apple a day keeps the doctor away'    следующим образом:
# в качестве ключей возьмите символы строки,
# а значениями пусть будут числа, соответствующие количеству вхождений данной буквы в строку.

          # Вариант с каждым элементом , т.е включая пробел
# A="An apple a day keeps the doctor away"
# B={i:A.count(i) for i in A}
# print(B)

          # Вариант используя только буквы строки ( без пробелов)
# A="An apple a day keeps the doctor away"
# A1=A.replace(" ","")
# print(A1)
# B={i:A1.count(i) for i in A1}
# print(B)




#6.	Ввести 10 чисел, данные числа добавить их во множество.
                #вариант 1
# import random
# A= set(random.randint(0,50) for i in range(10))
# print(A)
              #вариант 2

# A=10,34,23,14,23,67,8,3,49,0
# A1=set(A)
# print(A1)

              #Вариант3
# A1= int(input("ВВедите 1-е число:"))
# A2= int(input("ВВедите 2-е число:"))
# A3= int(input("ВВедите 3-е число:"))
# A4= int(input("ВВедите 4-е число:"))
# A5= int(input("ВВедите 5-е число:"))
# A6= int(input("ВВедите 6-е число:"))
# A7= int(input("ВВедите 7-е число:"))
# A8= int(input("ВВедите 8-е число:"))
# A9= int(input("ВВедите 9-е число:"))
# A10= int(input("ВВедите 10-е число:"))
# B=(A1,A2,A3,A4,A5,A6,A7,A8,A9,A10)
# B1=set(B)
# print(B1)



#7.	Найти самое длинное слово в строке.
# a="Найти самое длинное слово в строке"
# a_spl=a.split(" ")
# world=sorted(a_spl,key=len)
# print("Самое длинное слово-",world[-1])



#8.	Есть словарь песен группы Depeche Mode
# violator songsdict = { 'World in My Eyes': 4.76, 'Sweetest Perfection': 5.43, 'Personal Jesus': 4.56, 'Halo': 4.30, 'Waiting for the Night': 6.07, 'Enjoy the Silence': 4.6, 'Policy of Truth': 4.88, 'Blue Dress': 4.18, 'Clean': 5.68, }
#Выведите общее время звучания всех песен.
# Создайте список песен, время звучаниях которых больше 5 минут
# Создайте новый словарь тех песен, в название которых состоит из одного слова
# violator_songsdict = { 'World in My Eyes': 4.76,
#                        'Sweetest Perfection': 5.43,
#                        'Personal Jesus': 4.56,
#                        'Halo': 4.30,
#                        'Waiting for the Night': 6.07,
#                        'Enjoy the Silence': 4.6,
#                        'Policy of Truth': 4.88,
#                        'Blue Dress': 4.18,
#                        'Clean': 5.68, }
# sum=0
# song=[]
# for i in violator_songsdict:
#     sum+=violator_songsdict[i]
#     if violator_songsdict[i]>5:
#         song.append(i)
# new={}
# print("общее время звучания всех песен-",sum,"мин")
# print(song)
#
# for i in violator_songsdict:
#     key=i.split(" ")
#     if  len(key)==1:
#         n={i:violator_songsdict[i]}
#         new.update(n)
# print(new)





