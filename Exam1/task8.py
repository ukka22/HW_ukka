#8.	Вам передан массив чисел. Известно, что каждое число в этом массиве имеет пару, кроме одного: [1, 5, 2, 9, 2, 9, 1] => 5
mass=[1,5,2,9,2,9,1]

for  i in mass:
    count = mass.count(i) #посчитаем количество элементов
    if count<2:
     print(i)