#Напишите рукурсивную функцию которая осуществляет суммирование чисел в списке
#список должен быть сгенерирован из 10 чисел, каждое в диапазоне от 1 до 100
import random
def sum_number(N):
    if N != []:
      summ = N[0] + sum_number(N[1:])   # рекурсивный вызов этой же функции
      return summ                       # Прибавить к общей сумме первый элемент
    else:
      return 0

N=[random.randint(1,100) for i in range(10)]
print(N)
print(sum_number(N))