#创建一个类（Animal）【动物类】，类里有属性（名称，颜色，年龄，性别），类方法（会叫，会跑）
class Animal():
    name:str = "default"

    def __init__(self, name, colour, age, sex):
        '''类里有属性（名称，颜色，年龄，性别）'''
        self.name = name
        self.colour = colour
        self.age = age
        self.sex = sex

    def wow(self):
        '''类方法会叫'''
        print(f"{self.name} 会叫")

    def run(self):
        '''类方法会跑'''
        print(f"{self.name} 会跑")

        # 创建子类【猫】，继承【动物类】，
class Cat(Animal):
    # - 复写父类的__init__方法，继承父类的属性，
    # - 添加一个新的属性，毛发 = 短毛，
    def __init__(self, name, colour, age, sex, hair = "short hair"):
        self.name = name
        self.colour = colour
        self.age = age
        self.sex = sex
        self.hair = hair
        # - 添加一个新的方法， 会捉老鼠，
    def work(self):
        print("猫会捉老鼠")
        # - 复写父类的‘【会叫】的方法，改成【喵喵叫】
    def wow(self):
        print(f"{self.name} 喵喵叫")
# 创建子类【狗】，继承【动物类】，
# - 复写父类的__init__方法，继承父类的属性，
# - 添加一个新的属性，毛发=长毛，
class Dog(Animal):
    def __init__(self, name, colour, age, sex, hair = "long hair"):
        self.name = name
        self.colour = colour
        self.age = age
        self.sex = sex
        self.hair = hair
# - 添加一个新的方法， 会看家，
    def work(self):
        print("狗会看家")
# - 复写父类的【会叫】的方法，改成【汪汪叫】
    def wow(self):
        print(f"{self.name} 汪汪叫")
# 创建一个猫猫实例
cat = Cat("小花猫", "白色", "1", "公", "短发")
# - 调用捉老鼠的方法
cat.work()
# - 打印【猫猫的姓名，颜色，年龄，性别，毛发，捉到了老鼠】。
print(f"{cat.name},{cat.colour},{cat.age},{cat.sex},{cat.hair}","捉到了老鼠。")
# 创建一个狗狗实例
dog = Dog("小黄", "黄色", "7个月", "雌性", "长毛")
# - 调用【会看家】的方法
dog.work()
# - 打印【狗狗的姓名，颜色，年龄，性别，毛发】。
print(f"{dog.name},{dog.colour},{dog.age},{dog.sex},{dog.hair}")