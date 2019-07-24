""" Define a class Person and its two child classes: Male and Female. 
All classes have a method "getGender" which can print "Male" for Male class and "Female" for Female class. """

class Person:
    gender = "Unknown"

    def getGender(self):
        print(self.gender)

class Male(Person):
    gender = "Male"

    def getGender(self):
        print(self.gender)

class Female(Person):
    gender = "Female"

    def getGender(self):
        print(self.gender)

male = Male()
male.getGender()
female = Female()
female.getGender()
