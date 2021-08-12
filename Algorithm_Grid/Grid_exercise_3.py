s = input()
sum = 0
for i in range(len(s)):
    tmp = int(s[i])
    if tmp == 0 or tmp == 1:
        sum += tmp
    elif sum == 0:
        sum += tmp
    else:
        sum *= tmp
print(sum)