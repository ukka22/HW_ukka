# a= "привет "  #+  оператор сложения строк
# b= "Юля"
# print(a,b)
# print (a+b)
# print(5*a)                           # * это оператор создает несколько копий строки
# print(len(a))                        #считает число символов в строке включая пробелы

# name=input("введите Ваше имя")
# print("привет", name)
# print(3*name)


# s="программирование"
# print(s[0],s[4],s[-5]) # s[i], где s- строка, i- индекс
# # s[a:b] - b-не включается
# print(s[0:4],s[1:3],s[1:],s[:-3]) # положительная индексация начинается с 0,отриц- с -1
# # s[a:b:c] - где с- это шаг с которым будут выводится символы
# print(s[0:5:1], s[::1],s[0:5:2],s[::3])
# print(s[1:8:2])

# import random
# abc= random.randint(100,999)
# print(abc)
# abc=str(abc)
# a=int(abc[0])
# b=int(abc[1])
# c=int(abc[2])
# print(a+b+c)


s= "привет юля"
s_2="Привет Юля"
s_3="Привет юля"
#делаем строку заголовком
print(s.title())
#начинаем строку с заглавной буквы
print(s.capitalize())
# переводит строку в верхний регистр
print(s.upper())
#переводим строку в нижний регистр
print(s.lower())
#инверсия регистра
print(s_2.swapcase())
#проверяем является ли строки заголовками #заголовок - кажое слово с большой буквы
print(s.istitle())
print(s_2.istitle())
print(s_3.istitle())
# #создаем строку
# print("..".join(["a","b"]))
# #разбивает строку на список
# print("1_2_3".split("_"))
# a="Don't worry"
# print (a[::3])
# print (a[0]+a[-1])
# print(a.upper())




