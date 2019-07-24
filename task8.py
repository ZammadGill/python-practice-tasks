""" Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers """
def squareOddNumber(numbers_list):
    odd_numbers_square = [n * n for n in numbers_list if n % 2 != 0]
    print(odd_numbers_square)

numbers = [1,2,3,4,5,6,7,8,9]
squareOddNumber(numbers)
