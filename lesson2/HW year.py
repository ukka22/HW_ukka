year=int(input("введите год"))
if (year%4==0 and year%100!=0) or (year%400==0): #год делится на 4, но не делится на 100 или год делится на 100 и при этом еще на 400
    print(year, "- високосный год")
else:
    print(year,"год не високосный ")

