class Cat:
    def __init__(self, name, color):
        Cat.name = name
        Cat.color = color
    
    def meow(self):
        print(f"내 이름은 {self.name} , 색깔은 {self.color} 야")


nabi = Cat("나비","검정")
nabi.meow()