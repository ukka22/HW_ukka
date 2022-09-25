# d={}
# d={"dict":1,"dictionary":2}
# print(d)

 # метод создания словарей
# d=dict(short="dict",long="dictionary")
# d_2=dict([(1,1),(2,4)])
# print(d, "\n", d_2)


#
# d=dict.fromkeys(["a","b"])                  # создает словарь ключ с пустным значением
# d_2=dict.fromkeys(["a","b"],100)             # добавляет ко всем ключам одинаковые значения
# print(d,"\n", d_2)

#  #генератор словарей
# d={a:a**2 for a in range(7)}
# print(d)

# d= {1:2,2:4,3:9}
# d[4]=4**2         # имя ключа = значение  - всегда добавляется в конец словаря
# print(d[1])      # обращемся к имени ключа а печатаем значение
# print(d)
# d[2]=5
# print(d)           #{1: 2, 2: 5, 3: 9, 4: 16}
#
# print(d.get(1))    #2
#
# print(d.items())   #dict_items([(1, 2), (2, 5), (3, 9), (4, 16)])
#
# print(d.keys())    #dict_keys([1, 2, 3, 4])
#
# print(d.pop(1))    #2 - удаляет ключ, возвращая значение
# print(d)           #{2: 5, 3: 9, 4: 16}
#
# print(d.popitem()) #(4, 16) -удаляет и возвращает пару  ( с последнего)
# print(d)           #{2: 5, 3: 9}
#
# print(d.setdefault(2))   #5 возвращает значение ключа
# print(d.setdefault(1))   #None   - если нетключа такого нет то создает ключ со значене None
# print(d)                 #{2: 5, 3: 9, 1: None}
#
# print(d.values())        # dict_values([5, 9, None]) возвращает значения

  #удаление элемента из словаря
# dict={"яблоко":3,"слива":8, "арбуз":2}
# print(dict)
# del dict["слива"]
# print(dict)


#Вложенные словари

# position={"менеджер":{"директор","замдиректор"}, "учитель":{"специалист","методист","лектор"}}
# count1=len(position)
# count2=len(position["менеджер"])
# count3=len(position["учитель"])
# print(count3,count2,count1)


#f_is = key in D
#D – исходный словарь;
#key – ключ, наличие которого в словаре D нужно определить;
#f_is – результат логического типа. Если f_is=True, то ключ key присутствует в словаре. Если f_is=False, то ключа нету в словаре.

# dict={"яблоко":3,"слива":8, "арбуз":2}
# print(dict)
# #удалить элемент по ключу с проверкой
# key="яблоко"
# if key in dict:
#     del dict["яблоко"]
#     print(dict)
# key=5                           #припопытки удалить несуществующий ключ ошибка не генерируется
# if key in dict:
#     del dict[5]
#     print(dict)



#создание словаря из списков  ключей и значений

# num=dict(zip([1,2,3],["one","two","three"]))
# print(num)


# #обход словаря с помощью цикла for и вывод всех пар  ( ключ: значение)
# dict={1:"январь",2:"февраль",3:"март", 4:"апрель",5:"май"}
# for mn in dict:
   # print(mn,":",dict[mn], end=", ")


#    Cортировка по ключам
#Если возникает необходимость отсортировать словарь по ключам, то для этого можно использовать метод sort(),
# который используется для списков. Для этого предварительно нужно конвертировать представление ключей в список
# dict={"яблоко":3,"слива":8, "арбуз":2}
# key= dict.keys()    # получаем представление по ключам
# key=list(key)       #переводим в список
# print(key)
# key.sort()          #сортировка
# print(key)
# dict1={}
# for k in key:
#     print(k,":",dict[k])     #вывести перечень по отсортированным (ключ:значение )
#     dict1[k]=dict[k]         #сформировать новый словарь
# print(dict1)



#Создать словарь с ключами и значениями и вывести значение возраста
# person={"name":"Вася", "age": 33, "city": "Минск"}
# print(person)
# print(person["age"])


# Создайте словарь с ключами BMW, Tesla и списками из 3х моделей в качестве значений.
# Выведите первое и последнее значения каждого из ключей.
# car={"BMW":["x3","x5","x7"], "Tesla":["mod-1","mod-2","mod-3"]}
# print(car["BMW"][0],car["BMW"][2],"\n",car["Tesla"][0],car["Tesla"][2])


#Исправьте ошибки в коде, чтобы получить требуемый вывод. (Вывод True)
#d1 = {"a": 100. "b": 200. "c":300}
#d2 = {a: 300. b: 200, d:400}

# d1 = {"a": 100, "b": 200, "c": 300}
# d2 = {"a": 300, "b": 200, "d": 400}
#
# print(d1["b"] == d2["b"])

#Дан словарь с числовыми значениями. Необходимо их все перемножить и вывести на экран.

# dict={"яблоко":3,"слива":8, "арбуз":2}
# pr=1
# for i in dict:
#     pr*=dict[i]
# print(pr)


#Даны два списка одинаковой длины. Необходимо создать из них словарь таким образом,
# чтобы элементы первого списка были ключами, а элементы второго — соответственно значениями нашего словаря
# A=["Маша","Витя","Артем"]
# B=[13,12,10]
# AB=dict(zip(A,B))
# print(AB)


#Создайте словарь из строки 'pythonist' следующим образом:
# в качестве ключей возьмите буквы строки, а значениями пусть будут числа, соответствующие количеству вхождений данной буквы в строку
#  Вариант 1
# a="pythonist"
# A=list(a)
# print(A)
# B=[]
# for i in A:
#     C=A.count(i)
#     B.append(C)
# print(B)
# AB=dict(zip(A,B))
# print(AB)
#
#  # Вариант 2
# a="pythonist"
# A={i:a.count(i) for i in a}
# print(A)

dict={1:"январь",2:"февраль",3:"март", 4:"апрель",5:"май"}

print(list(dict.keys()))