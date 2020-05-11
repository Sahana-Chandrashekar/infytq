#PF-Prac-9
def generate_dict(n):
    d = {}
    for i in range(1,n+1):
        d[i] = i*i
    return d
number=20
print(generate_dict(number))
