import string
alpha = input()

array = list(string.ascii_lowercase)
result_array = [0]*len(array)
for x in alpha:
    for i in range(len(array)):
        if x == array[i]:
            result_array[i] += 1
for i in range(len(result_array)):
    print(result_array[i],end = ' ')