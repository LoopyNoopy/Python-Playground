class personFile:
    def __init__(self,name,age,height):
        self.name = name
        self.age = age
        self.height = height
        
myName = raw_input("What is your name? ")
myAge = input("What is your age? ")
myHeight = raw_input("What is your height? ")

myself = personFile(myName,myAge,myHeight)

print myself.name
print myself.age
print myself.height