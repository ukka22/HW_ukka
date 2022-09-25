#Если в функцию передаётся кортеж, то посчитать длину всех его слов.
#Если список, то посчитать кол-во букв и чисел в нём.
#Число – кол-во нечётных цифр.
#Строка – кол-во букв.
#Сделать проверку со всеми этими случаями
def function(F):

    if type (F)==tuple:
         l = 0
         for i in F:
            if type (i) ==str:
                l +=len(i)
         return l
    if type (F)==list:
         let=0
         numb=0
         for i in F:
             if type (i)==str:
                 for j in i :
                     let+=1
             else:
                 numb+=1
         return let, numb
    if type (F) ==int:
        c=0
        for i in str(F):
                i = int(i)
                if i%2!=0:
                    c+=1
        return c
    if type (F)==str:
        s=0
        for i in F:
            if i.isalpha():
                s+=1
        return s

print(function(("I","live","in","Minsk",20,"years")))
print(function([25, "Ivan",96,"Egor",745]))
print(function(54698))
print(function("hello world"))