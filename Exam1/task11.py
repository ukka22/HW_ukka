#11.Дана строка [“hello my friend”, “my name is”, “house”, “cat”, “dog”].
# В новый список добавить элементы, которые содержат пробел.
mass=["hello my friend", "my name is", "house", "cat", "dog"]
a=" "
mass1=[]
for i in mass:
    if a in i:  # проверяем каждый элемент через прохождение переменной по списку  на наличие в нем пробелов
        mass1.append(i)
print(mass1)
