a=int(input("сторона треугольника а="))   #вводим три стороны треугольника
b=int(input("сторона треугольник b="))
c=int(input("сторона треугольника с="))
#треугольника не существует в том случае, когда одна сторона будет по длине больше чем
# длина в сумме двух других сторон.
if (a>b+c) or (b>a+c) or (c>a+b):
    print("Нет,тругольника со сторонами", a,b,c, " не существует ")
else:
    print("Да, трегольник со сторонами", a,b,c, "-существует")
    if a==b==c:                             # если все стороны равно - то треугольник равносторонний
        print("И он - равносторонний")
    elif  (a==b) or (a==c) or (b==c):       # если равны обе стороны - равнобедренный
        print("И он - равнобедренный")
    else:
        print("И он - разносторонний")      #все стороны разные- разносторонний

