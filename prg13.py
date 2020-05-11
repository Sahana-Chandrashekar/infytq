'''
Write a python function which accepts three numbers and returns True if
a.one of the three numbers is "close" to any one of the other numbers (differing from a number by at most 1), and
b.Number that is left out is "far", differing from both other values by 2 or more.
Return false if the above mentioned conditions are not satisfied.
Sample Input	Expected Output
  4,1,3	           True
  5,6,7	           False
'''
#PF-Prac-13
def close_number(num1,num2,num3):
    if num1==num2 or num1==num3 or num2==num3 or num2!=num1+1 or num3!=num1+2:
        return True
    return False
print(close_number(3,0,5))
