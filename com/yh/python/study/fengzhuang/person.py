class Person:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        return "我的名字是%s体重是%s" % (self.name, self.weight)

    def run(self):
        self.weight -= 0.5

    def eat(self):
        self.weight += 1


xiaoming = Person("小明", 70)
xiaoming.run()
xiaoming.eat()

print(xiaoming)
