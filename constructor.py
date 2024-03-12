class person:
    def __init__(self,name):
        self.name = name
    def talk(self):
        print(f"Hi,I am {self.name}")


john = person("John Smith")
john.talk()
ron = person("Ron weasely")
ron.talk()
dumb = person("Dumb Nigga")
dumb.talk()