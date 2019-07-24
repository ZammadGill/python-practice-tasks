""" Write a program that accepts a sentence and calculate the number of letters and digits """

def noOfLettersAndDigits():
    string = input("Enter String: ")
    letters = sum(c.isalpha() for c in string)
    digits = sum(d.isdigit() for d in string)
    print("LETTERS", letters)
    print("DIGITS", digits)

noOfLettersAndDigits()
