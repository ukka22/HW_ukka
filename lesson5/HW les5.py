#Массив из 7 цифр.
# Если четных цифр в нем больше чем нечетных, то найти сумму всех его цифр,
# если нечетных больше, то найти произведение 1 3 и 6 элемента.


import random
mass = [random.randint(0,20) for i in range(7)]
print(mass)
mass1=[]
mass2=[]
sum=0
for i in mass:
        if i % 2 == 0:
            mass1.append(i)
        else:
            mass2.append(i)
print(mass1)
print(mass2)
if len(mass1)>len(mass2):
    for i in mass:
        sum+=i
    print("Сумма всех чисел:", sum)
else:
    pr=mass[0]*mass[2]*mass[5]
    print("Произведение 1,3 и 6 элемента :",pr)

