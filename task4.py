""" Define a class which has at least two methods:

getString: to get a string from console input
printString: to print the string in upper case.

Also please include simple test function to test the class methods.
 """
class MyString:
    title = ""
    string = ""

    def __init__(self, title):
        self.title = title

    def getString(self):
        self.string = input("Enter String: ")

    def printString(self):
        print(self.string.upper())

    def testString(self):
        print(self.title)
        self.getString()
        self.printString()

myObject = MyString("My String Class")
myObject.testString()
