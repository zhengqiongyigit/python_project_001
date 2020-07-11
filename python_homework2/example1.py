#创建一个person类
# 属性：姓名、性别、年龄、存款金额
# 方法：吃、睡、跑、赚钱
#
# 创建FunnyMan类
# 继承父类person的所有属性和方法
# 现在一个方法，fun（）搞笑
#
# 创建SingerMan类
# 继承父类Person的所有属性和方法
# 复写方法、赚钱、传参（money）
class Person():
    name:str = "default"
    gender:str = "default"
    age:int = 20
    money:float = 1000

    # def set_name(self, name):  这个函数定义相当于下面的init函数中的name定义
    #     self.name = name

#以后python函数中的类中的属性可以用init函数来定义，比较简单
    def __init__(self,name, gender, age, money):
        self.name = name
        self.gender = gender
        self.age = age
        self.money = money
       # self.__money = money  私有属性

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

    def run(self):
        print(f"{self.name} is running")

    def make_money(self):
        print(f"{self.name} could make money")

class FunnyMan(Person):
   def fun(self):
       print(f"{self.name} is very funny")


class SingerMan(Person):
    def make_money(self,moneynum):
        print(f"{self.name} could make money {moneynum} ")

singer = SingerMan("jerry","男",28,20000)

funnyman = FunnyMan("st","男", 30 ,20000)
print(funnyman, name)
funnyman.eat()
funnyman.fun()
#print(dir(p))  可以打印p的所有的属性

p = Person("lili", "女", 18, 1000)
#p.set_name("tom")  此函数与上面的函数需要对应，后期我们就不用此函数了
print(p.name)
p.eat()
