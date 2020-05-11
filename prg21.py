'''
Tom is working in a shop where he labels items. Each item is labelled with a number between num1 and num2(both inclusive). Since Tom is also a natural mathematician,
he likes to observe patterns in numbers. Tom could observe that some of these label numbers are divisible by other label numbers.
Write a Python function to find out those label numbers that are divisible by another label number and display how many such label numbers are there totally.
'''
#PF-Prac-21
def check_numbers(num1,num2):
    num_list=[]
    count = 0
    for i in range(num1,(num2//2)+1):
        num_list.extend([x for x in range(i+1,num2+1) if x%i==0])
        
    num_list=set(num_list)
    count=len(num_list)
    return [num_list,count]

num1=2
num2=20
print(check_numbers(num1, num2))
