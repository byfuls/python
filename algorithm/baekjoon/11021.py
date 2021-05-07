import sys

count = int(input())
input = sys.stdin.readline
for v in range(1, count+1):
    x, y = map(int, input().split())
    print(f"Case #{v}: {x} + {y} = {x+y}")