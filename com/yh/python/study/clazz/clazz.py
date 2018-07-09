class Cat:
    def __init__(self):
        """
        python定义属性的方法
        """
        self.name = "Tom"

    def eat(self):
        print("小猫爱吃鱼")

    def drink(self):
        print("小猫爱喝水")


cat = Cat()
cat.drink()
cat.eat()
print(cat.name)
