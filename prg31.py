'''
Given a list of integers and a number. Write a python function to find and return the sum of the elements of the list.
Note: Don't add the given number and also the numbers present before and after the given number in the list.

     Sample input	                    Expected output
list=[1,2,3,4], number=2	                4
list=[1,2,2,3,5,4,2,2,1,2],number=2	        5
list=[1,7,3,4,1,7,10,5],number=7	        9
list=[1,2,1,2],number=2	                        0
'''
#PF-Prac-31
def sum_of_elements(num_list,number):
    result_sum = 0
    p = pos(num_list,number)
    for i in range(len(num_list)):
        if i not in p:
            result_sum += num_list[i]
    return result_sum

def pos(num_list,number):
    temp = []
    for i in range(0,len(num_list)):
        if number == num_list[i]:
            temp.append(i-1)
            temp.append(i)
            temp.append(i+1)
    return temp

num_list=[1,7,3,4,1,7,10,5]
number=7
print(sum_of_elements(num_list, number))
