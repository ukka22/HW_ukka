# выставить оценник учащимся за тест в соответсвии с обьемом решенных примеров. при условии что
#  решено верно меньше 50% - неудовлетворительно
# решено (50-64)%- удовлетворительно
# решено (65-89)%- хорошо
# решено больше 90% - отлично

task=int(input("количество задач/примеров в тесте"))
done=int(input("количество верно решенных задач/примеров"))
if (done<task/2):
    print("неудовлетворительно")
elif (done>=task/2) and (done<task/100*65):
    print("удовлетворительно")
elif (done>=task/100*65) and (done<task/100*90):
    print("хорошо")
elif (done>task/100*90) and (done<=task):
    print("отлично!")
else:
    print("данные введены некорректно")

