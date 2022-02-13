n, k = map(int, input().split())

list_a = list(map(int, input().split()))
list_b = list(map(int, input().split()))

sort_list_a = sorted(list_a)
sort_list_b = sorted(list_b, reverse=True)

for i in range(k):
    if sort_list_a[i] < sort_list_b[i]:
        sort_list_a[i], sort_list_b[i] = sort_list_b[i], sort_list_a[i]

print(sum(sort_list_a))