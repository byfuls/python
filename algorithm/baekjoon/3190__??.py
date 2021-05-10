import sys

n = int(input())
board = [[0 for col in range(n)] for row in range(n)]
appleCount = int(input())
for _ in range(appleCount):
    appleX, appleY = map(int, sys.stdin.readline().split())
    board[appleX][appleY] = "apple"
print(board)

directionCount = int(input())
direction = []
for _ in range(directionCount):
    time, dr = sys.stdin.readline().split()
    time = int(time)
    direction.append([time, "left" if dr == "L" else "right"])
print(direction)