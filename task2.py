""" Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 1000 and 2000 (both included) """
def findNumbersList(n1, n2):
    numbers_list = []
    for x in range(n1, n2 + 1):
        if (x % 7 == 0
            and x % 5 != 0):
                numbers_list.append(x)
    print(numbers_list)   

findNumbersList(1000, 2000)
