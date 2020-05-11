'''
Write a python function to find out whether a number is divisible by the sum of its digits. If so return True,else return False.
Sample Input	Expected Output
   42	              True
   66	              False
'''
#PF-Prac-23
def divisible_by_sum(number):
    temp = number
    s = 0
    while number != 0:
        rem = number%10
        s += rem
        number = number//10
    if temp%s == 0:
        return True
    else:
        return False

number=25
print(divisible_by_sum(number))
