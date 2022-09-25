#Массив из 7 цифр.
# Если четных цифр в нем больше чем нечетных, то найти сумму всех его цифр,
# если нечетных больше, то найти произведение 1 3 и 6 элемента.
import random
mass= [random.randint(0,20)for i in range(7)]
print(mass)
count1=0
count2=0
sum=0
for i in mass:
    if i%2==0:
        count1+=1
    else:
        count2+=1
print("Четных:", count1, "Нечетных:", count2)
if count1 > count2:
    for i in mass:
        sum+=i
    print("Сумма:",sum)
else:
    pr=mass[0]*mass[2]*mass[5]
    print("Произведение:", pr)





