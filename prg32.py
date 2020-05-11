'''
Given an integer n, write a python function to return true,if it is possible to
representit as a sum of the squares of two different integers,else return false.
'''
#PF-Prac-32
def check_squares(number):
    i = 1
    while i*i <= number:
        j=1
        while j*j <= number:
            if i*i+j*j==number:
                return True
            j += 1
        i += 1
    return False

number=68
print(check_squares(number))
