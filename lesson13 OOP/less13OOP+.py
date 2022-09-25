#Переопределение метода в классе:
# class Car:
#     #создание методов класса
#     def __str__(self):
#         return "Car class Object"
#     def  start(self):
#         print("двигатель заведен")
# car_a=Car()
# print(car_a)


# class Phone:
#  @staticmethod
#  def model_hash(model):
#      if model=="1785":
#          return 34565
#      elif model=="K498":
#          return 45567
#      else:
#          return None
# print(Phone.model_hash("1785"))

# my_phone= Phone ("red", "1785")
# my_phone.check_sim("MTS")

# class Human:
#     default_name='Yulia'
#     default_age=43
#     def __init__(self,name=default_name,age=default_age):
#         #публичные
#         self.name=name
#         self.age=age
#         #приватные
#         self.__money=0
#         self.__house=None
#     def info(self):
#         print(f"Name:{self.name}")
#         print(f"Age: {self.age}")
#         print(f"Money: {self.__money}")
#         print(f"House: {self.__house}")
#     @staticmethod
#     def default_info():
#         print(f"Default name: {Human.default_name}")
#         print(f"Default age: {Human.default_age}")
#     def earn_money(self,amount):
#         self.__money+=amount
#         print(f"Earned {amount} money! Current value: {self.__money}")
#
# # Human.default_info()
#
# # persone_1=Human()    Name:Yulia  Age: 43 Money: 0 House: None
# # persone_1.info()
#
# persone_1 = Human("Sasha",27)   #Name:Sasha   Age: 27   Money: 0  House: None
# persone_1.info()
#
# persone_1.earn_money(5000)
# persone_1.earn_money(20000)
# persone_1.info()

class Calculator:
    def valdate_numbers(self, first_number, second_number):
        is_valid_first_number= isinstance(first_number,int) or isinstance(first_number,float)
        is_valid_second_number= isinstance(second_number,int) or isinstance(second_number,float)
        if  is_valid_first_number and is_valid_second_number:
            print("Valid")
        else:
            raise Exception ("Not Valid")
my_calc=Calculator()
my_calc.valdate_numbers(1,"lkj")
