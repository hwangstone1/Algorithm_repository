# 특수문자을 replace 내장함수를 통해 치환한다 .
# 특수문자를 '.' 로 치환하여 , 문자열의 길이를 잰다.
cro_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
data = input()
for i in cro_list:
    data = data.replace(i, '.')
print(len(data))
