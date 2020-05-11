'''
Given two positive integers. Write a python function to return the GCD of the given numbers.
Sample Input	Expected Output
 14 and 35	        7
800 and 2800	       400
'''
#PF-Prac-24
def find_gcd(num1,num2):
    if num1>num2:
        small = num2
    small = num1
    for i in range(1,small+1):
        if (num1%i==0 and num2%i==0):
            HCF = i
    return HCF

num1=45
num2=9
print(find_gcd(num1,num2))
