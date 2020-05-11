'''
Given a list of numbers, write a python function to exchange the first n/2 elements of a list with the last n/2 elements.
The function should return the new list.
n represents the number of elements in the list. Assume that it will always be even.

Sample Input	            Expected Output
[1,2,3,4,5,6,7,8,9,10]	[10,9,8,7,6,1,2,3,4,5]
'''
#PF-Prac-29
'''
def exchange_list(number_list):
    l=len(number_list)
    half=l//2
    l1=number_list[l:half-1:-1]
    l2=number_list[0:half]
    number_list=l1+l2
    return number_list
'''
def sample(l):
    n = len(l)
    return l[n//2:][::-1]+l[:n//2]
     
number_list=[1,2,3,4,5,6]
print(exchange_list(number_list))
