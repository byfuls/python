import sys

loop = int(input())
visited = [False]*loop
graph = [[0]*loop for _ in range(loop)]

for x in range(loop):
    row = sys.stdin.readline().strip()
    for y, val in enumerate(row):
        graph[x][y] = int(val)

print(graph)