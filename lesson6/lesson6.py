# создаем пусто йсписок
# elements = list()
# print(elements)

import random # генератор рандомного списка
# c= [random.randint(0,100) for i in range (10)]
# print(c)
#
# print(c[0])
# print(c[-1])
# print(c[5])
# print(c[0:2])
# print(c[1:5:2])
# print(c[0]+c[1])

# elements = []
# elements.append("a")
# elements.append(1)
# print(elements)

#добавление в список

# elements = [1,3,"a",6,"b"] # желательно работать только с положительной индексацией
# elements.insert(1,"B") # до запятой позици по индексу, после запятой - добавляемый элемент
# print(elements)
# elements.insert(1,"С")
# print(elements)

# изменить/заменить элемент списка

# elements = [1,3,"a",6,"b"]
# elements [1] = "B" #в [] - это индекс элемента который заменяем , после = элемент которым заменяем
# print(elements)


# удаление элемента

# elements = [1,3,"a",6,"b"]
# del elements [1]     # удаляет элемент по индексу
# print(elements)
# elements.remove("a")  # удаляет элемент по имени и удаляет первое вхождение в список
# print(elements)

# проверка есть ли элемент в списке

# elements = [1,3,"a",6,"b","abc",13,567]
# if "abc" in elements:
#     print("Yes")

# обьединение списков

# d=[1,3,"a",6,"b","abc",13,567]
# e=["привет мир"]
# d.extend(e)       # не возвращает новый список а дополняет текущий
# print(d)
# d.extend("1123")
# print(d)

#копирование списка в Python - это копирование не удачное так как при изменении a изменияется и b

# a = [1,3,"a",6,"b"]
# b=a                  #переменной b присваивается не значение списка а его адрес
# a.append(5)
# b.append(6)
# print(a,b)


# правильное копирование

# a=["слон", "кот","змея"]
# b=a.copy()
# b.append("тигр")
# print(a,b)

 #копирование часть списка через срез
# a = ["слон", "кот", "змея"]
# b=a[2]
# print(a,b)

# удаление всех элементов
# a = ["слон", "кот", "змея"]
# a.clear()
# print(a)

 #copy
# a = ["слон", "кот", "змея","кот"]
# b=a.copy()
# print(id(a),id(b),a,b)

#count
# a = ["слон", "кот", "змея","кот"]
# b=a.count("кот")
# print(b)

#pop
# a = ["слон", "кот", "змея", "кот"]
# a.pop(2)
# print(a)


# вложенные списки
# elements = [["яблоки",50],["апельсины",190],["груши",100]]
# print(elements[0])
#
# print(elements[1][0])

# произвольный список , вывести в обратном порядке
# a=[3,8,45,34,23]
# a.reverse()
# print(a)


#дан список некоторых целых чисел, найдите значение 20 в нем, если оно есть заменитт на 200
# Обновите список только при первом вхождении числа 20.
# a=[34,56,20,67,4,20,32]
# # b=a.index(20)
# # a[b]=200
# # print(a)
# # c=len(a)
# # print(len(a))

#Найти совпадающие элементы двух списков.
#Эти значения записать в новый список
# a = [5,[1,2],2,'r',4,'ee']
# b = [4,'we','ee',3,[1,2]]
# c=[]
#
# for i in b:
#     if i in a:
#         c.append(i)
# print(c)


#Даны 2 списка:
#Выполнить следующие операции:
# - Сложить два списка
# - Добавьте элемент 6 на 3 позицию в 2м списке.
# - Удалите все текстовые переменные
# - Посчитайте количество элементов спика
# a = [4,6,'pу',78]
# b = [44,"hello",56,"exept",3]
# a.extend(b)
# a.insert(2,6)
# print(a)
# for i in a:
#     if type (i) is str:
#         a.remove(i)
# print(a)
# print(len(a))














