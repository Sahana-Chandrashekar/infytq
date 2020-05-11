'''
Given a string, write a python function to return True if the strings "mat" and "jet" appear the same number of times in the given string, else return False.
Note: Perform case insensitive string comparison wherever necessary.

Sample Input	                     Expected Output
Jet on the Mat but mat is too long	False
mat jet Jet Mat	                        True
'''
#PF-Prac-26
def check_occurence(string):
    s = string.split(' ')
    temp1=s.count('Mat')+s.count('mat')
    temp2=s.count('Jet')+s.count('jet')
    if temp1 == temp2:
        return True
    return False
        
string="Jet on the Mat but mat is too long"
print(check_occurence(string))
