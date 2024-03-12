class mammal:
     def walk(self):
        print("Walk")


class Dog(mammal):
    pass


class Cat(mammal): 
    pass

dog1 = Dog()
dog1.walk()
cat1 = Cat()
cat1.walk()
