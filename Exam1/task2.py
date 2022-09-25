#2 написать программу для вычисления значения выражений.
# Проверитьправильность выполнения задания с помощью тестовых значений
a=int(input("a="))
y=((((1+a+a**2)/(2*a+a**2))+2-((1-a+a**2)/(2*a-a**2)))**-1*(5-2*a**2))
print(y)

# import math
# a=int(input("a="))
# b=int(input("b="))
# c=int(input("c="))
#
# y=0.25*int(math.sin(a+b-c)+math.sin(b+c-a)+math.sin(c+a-b)-math.sin(a+b+c))
#
# print(y)