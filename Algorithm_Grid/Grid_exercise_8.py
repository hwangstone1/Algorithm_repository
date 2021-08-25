# rope
n = int(input())
rope = []
Max_w =[]
for _ in range(n):
    rope.append(int(input()))
rope = sorted(rope, reverse= True) # rope.sort(reverse = True)
print(rope)
for i in range(n):
    Max_w.append(rope[i]*(i+1))
print(max(Max_w))
