#PF-Prac-11
def find_upper_and_lower(sentence):
    result_list = [0,0]
    for i in sentence:
        if i >= 'A' and i<='Z':
            result_list[0] += 1
        elif i >= 'a' and i<='z':
            result_list[1] += 1
    return result_list

sentence="Come Here"
print(find_upper_and_lower(sentence))
