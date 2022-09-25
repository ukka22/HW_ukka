#Два метода в классе, один принимает в себя либо строку, либо число.
#Если я передаю строку, то смотрим:
#если произведение гласных и согласных букв меньше или равно длине слова, выводить все гласные, иначе согласные;
#если число то, произведение суммы чётных цифр на длину числа.
#Длину строки и числа искать во втором методе.

class Result:
    def __init__(self):
        self.a = []
        self.b = []
        self.n_a = 0
        self.n_b = 0
        self.plus = 0

    def func(self,s):

        if type(s) is  str:
            for i in s:
                if i  in "aeouiy":
                    self.a.append(i)
                    self.n_a+=1
                else:
                    self.b.append(i)
                    self.n_b+=1
            print("количество гласных-",self.n_a)
            print("количество согласных-", self.n_b)
            print("длина слова-",self.func1(s))
            if (self.n_a*self.n_b)<=self.func1(s):
                print("гласные-",self.a)
            else:
                print("соглласные-",self.b)
        elif type(s) is  int:
            for i in str(s):
                i=int(i)
                if (i%2)==0:
                    self.plus+=i
        print (self.plus*self.func1(s))
    def func1(self,s):
        return len(str(s))
result=Result()
c= input("введите данные")
if c.isalpha():
    result.func(c)
elif c.isdigit():
    result.func(int(c))
