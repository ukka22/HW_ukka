#Дан список list=[15,48,'hello',6,19,'world’].
#Все числа этого списка проверить на чётность. Если число чётное, то посчитать сумму его цифр. Если нечётное, то заменить  его на 1 в списке.
#Все слова: посчитать количество гласных и согласных.Вывести всё на экран.

# list=[15,48,"hello",6,19,"world"]
# sum=0
# list1=[]
# vow=["a","e","i","o","u","y"]
# list_vow=[]
# list_cons=[]
# for i in list:
#     if type(i) is not str and i%2==0:     # если тип переменной не строка и если число четное
#         sum+=i
#     elif type(i) is not str and i%2!=0:
#         ind=list.index(i)                 # находим индекс нечетной переменной в списке
#         list[ind]=1                       # заменяем по этому индексу на число 1
#     elif type(i) is  str:
#         for a in i:
#            if a in vow:
#             list_vow.append(a)
#            else:
#             list_cons.append(a)
# print(sum)                                # сумма четных чисел списка
# print(list)                               # список с замененными нечетными числами на 1
# print("количество гласных-",len(list_vow))
# print("количество согласных-",len(list_cons))



list=[15,48,"hello",6,19,"world"]
sum=0
list1=[]

list_vow=[]
list_cons=[]
list1=[]
for i in list:
    if type(i) is not str and i%2==0:     # если тип переменной не строка и если число четное
        sum+=i
    elif type(i) is not str and i%2!=0:
        ind=list.index(i)                 # находим индекс нечетной переменной в списке
        list[ind]=1                       # заменяем по этому индексу на число 1
    else:
        list1.append(i)
print(sum)
print(list)
vow=["a","e","i","o","u","y"]
list2="".join(list1)
print(list2)
for j in list2:
    if j in vow:
        list_vow.append(j)
    else:
        list_cons.append(j)
print("количество гласных-",len(list_vow))
print("количество согласных-",len(list_cons))


