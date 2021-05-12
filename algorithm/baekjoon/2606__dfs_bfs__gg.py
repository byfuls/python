from sys import stdin

startingPoint = 1
vertex = int(input())
couple = int(input())
graph = [[0]*(vertex+1) for _ in range(vertex+1)]

for _ in range(couple):
    x, y = map(int, stdin.readline().split())
    graph[x][y] = 1
    graph[y][x] = 1

visited = [False]*(vertex+1)
dfsCount = 0
def dfs(start):
    global dfsCount
    visited[start] = True
    for i in range(1, vertex+1):
        if not visited[i] and graph[start][i] == 1:
            dfsCount += 1
            dfs(i)

dfs(startingPoint)
print("dfs: ", dfsCount)

visited = [False]*(vertex+1)
bfsCount = 0
def bfs(start):
    global bfsCount
    visited[start] = True
    queue = [start]
    while queue:
        start = queue.pop(0)
        for i in range(1, vertex+1):
            if not visited[i] and graph[start][i]:
                queue.append(i)
                visited[i] = True
                bfsCount += 1

bfs(startingPoint)
print("bfs: ", bfsCount)
