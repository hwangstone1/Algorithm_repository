"""
10 20 30 40
n = 2  == > 10 + 20 == 30
n = 3  == (10+20) + (10+20+30)  = 30 + 60 == 90
n = 4 == (10+20) + (10+20+30) + (10+20+30+40) == sum(n-1) +

"""
import heapq
result = 0
heap = []
n = int(input())
for i in range(n):
    data = int(input())
    heapq.heappush(heap, data)

while len(heap) != 1:
    one = heapq.heappop(heap)
    two = heapq.heappop(heap)
    print(one, two)
    tmp = one+two
    result += tmp
    heapq.heappush(heap, tmp)

print(result)