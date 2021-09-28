# 느리지만 간단한 구현
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())

graph = [[] for i in range(n+1)]
visit = [False] * (n+1)
distance = [INF] * (n+1)

for _ in range(m):
    x, y, z = map(int, input().split())
    # x번 노드에서 y번 노드로 가는 비용 z
    graph[x].append((y, z))


def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n+1):
        if distance[i] < min_value and visit[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    distance[start] = 0
    visit[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]

    for i in range(n-1):
        now = get_smallest_node()
        visit[now] = True
        for j in graph[now]:
            cost = distance[now] + j[1]

            if cost < distance[j[0]]:
                distance[j[0]] = cost

dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])


