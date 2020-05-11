'''
Write a Python function to rotate the list of elements by N positions. The function should return the rotated list.
Sample Input	                           Expected Output
Input list: [1, 2, 3, 4, 5, 6]             [5, 6, 1, 2, 3, 4]
Number of positions to be rotated = 2
Input list: [1, 2, 3, 4, 5, 6]             [3, 4, 5, 6, 1, 2]
Number of positions to be rotated = 4
'''
#PF-Prac-16
def rotate_list(input_list,n):
    output_list=[]
    for item in range(len(input_list) - n, len(input_list)): 
        output_list.append(input_list[item])
    for item in range(0, len(input_list) - n):  
        output_list.append(input_list[item])
    return output_list

input_list= [1,2,3,4,5,6]
output_list=rotate_list(input_list,4)
print(output_list)
