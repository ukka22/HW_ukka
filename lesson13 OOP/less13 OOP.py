# class Car:
#     pass
# car_object=Car()    #создадим объект класса Car
# print(dir (Car))


# class Car:
#     color='grey'
#     def turn_on (self):
#         pass
#
#     def ride(self):
#         pass
# car_object=Car()
# print(dir (Car))   #Список атрибутов класса / объекта можно получить с помощью команды dir()



# class Car:
#     default_color='grey'   #Статические поля.   переменные, которые объявляются внутри тела класса и создаются тогда
#     default_weight=500     #, когда создается класс. Создали класса - создалась переменная
#     def __init__(self, color,model):    #Динамические поля
#         self.color=color                #переменные, которые создаются на уровне экземпляра класса.
#         self.model=model                #Нет экземпляра - нет его переменных. Для создания динамического свойства необходимо обратиться к self внутри метода
#
# car_object=Car("red","lenovo")


#Служебное слово self - это ссылка на текущий экземпляр класса.
# Как правило, эта ссылка передается в качестве первого параметра метода Python:


#                Задание №1
#Создайте класс Example. В нём пропишите 3 (метода) функции.
# Две переменные задайте статически, две динамически.
# Первая функция: создайте переменную и выведите её
# Вторая функция: верните сумму 2-ух глобальных переменных
# Третья функция: верните результат возведения первой динамической переменной во вторую динамическую переменную
# Создайте объект класса.
# Напечатайте обе функции
# Напечатайте переменную a


# class Example:
#     a=2   #статические поля явлюятся глобальными переменнными так как они пишутся вне функции
#     b=3
#     def __init__(self, x,y):
#         self.x=x
#         self.y=y
#     def func(self):
#         self.c=5
#         print(self.c)
#
#     def func1(self):
#         return self.a+self.b
#
#     def func2(self):
#         return self.x**self.y
#
# example_object= Example(4,2)
# print(example_object.a)
# print(example_object.func1())
# print(example_object.func2())
# example_object.func()



                    #Калькулятор.
#Создайте класс, где реализованы функции(методы) математических операций.
#А также функция, для ввод данных

class Calcul:
    def __init__(self):
        self.func4()
    def func(self):
        return self.a+self.b
    def func1(self):
        return self.a-self.b
    def func2(self):
        return self.a*self.b
    def func3(self):
        if self.b==0:
            return "error"
        else:
            return self.a/self.b
    def func4(self):
        self.a =int(input("Введите первое число:"))
        self.b = int(input("Введите второе число:"))
while True:

    x = input("введите знак операции (+,-,*,/), 0-выход:")

    if x == "0":
        break
    calcul = Calcul()
    if x == "+":
        print(calcul.func())
    if x == "-":
            print(calcul.func1())
    if x == "*":
        print(calcul.func2())
    if x == "/":
            print(calcul.func3())