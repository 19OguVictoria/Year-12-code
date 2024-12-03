class Dog():
    def __init__(self, myName, myColour):
        self.name = myName
        self.colour = myColour

    def bark(self, barkTimes):
        for n in range(barkTimes):
            print("Bark!")

    def setColour(self, myColour):
        self.colour = myColour

    def setName(self, myName):
        self.Name = myName

    def getColour(self):
        return self.colour

    def getName(self):
        return self.name



myDog1 = Dog("Unknown", "Colour")
myDog1.bark(5)
if myDog1.getColour() == "Colour":
    print(f"Please enter a colour for {myDog1.name}")
    newColour = input()
    myDog1.setColour(newColour)
print(myDog1.getName(),"is now set to", myDog1.getColour())
if myDog1.getName() == "Unknown":
    print(f"Now that this dog is being renamed, please enter a new name for {myDog1.name}")
    newName = input()
    myDog1.setName(newName)
print(myDog1.setName(), "is now ", myDog1.getName(), " as it moves in to its forever home")

class Puppy(Dog):
    shoesChewed = 0
    def __init__(self, myName, myColour, myDob):
        super().__init__(myName, myColour)
        self.dob = myDob

    def chewShoe(self, myShoesChewed):
        self.shoesChewed = self.shoesChewed + myShoesChewed

    def getShoesChewed(self):
        return self.shoesChewed

    def detDob(self):
        return self.Dob

    def bark(self, barkTimes):
        for n in range(barkTimes):
            print("Yap!")
