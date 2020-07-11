class Person:
    name:str = "default"
    gender:str = "default"
    age:int = 20
    money:float = 1000

    def set_name(self, name):
        self.name = name

    def eat(self):
        print("is eating")

    def sleep(self):
        print("is sleeping")

    def run(self):
        print("is running")

    def make_money(self):
        print("could make money")

p = Person("lili", '女', 18, 1000)
p.set_name("tom")
print(p.name)

p1 = Person()
p1.set_name("jon")
print(p1.name)


