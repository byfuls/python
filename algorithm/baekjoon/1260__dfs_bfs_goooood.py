import sys
input = sys.stdin.readline

vertex, line, startingPoint = map(int, input().split())
graph = [[0]*(vertex+1) for _ in range(vertex+1)]       # 해당 정점에서 연결될 정점을 설정하기 위한 초기화 작업
visited = [False]*(line+1)                              # 이동 경로 판단용
for _ in range(line):
    x, y = map(int, input().split())
    graph[x][y] = 1 # 단방향 기준
    graph[y][x] = 1 # 양방향 기준

def dfs(start):
    visited[start] = True
    print(start, end=" ")
    for i in range(1, vertex+1):
        if not visited[i] and graph[start][i] == 1:
            dfs(i)

def bfs(start):
    visited[start] = False
    queue = [start]
    while queue:
        start = queue.pop(0)
        print(start, end=" ")
        for i in range(1, vertex+1):
            if visited[i] and graph[start][i] == 1:
                queue.append(i)
                visited[i] = False

dfs(startingPoint)
print()
bfs(startingPoint)