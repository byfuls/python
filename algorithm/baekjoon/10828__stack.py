import sys

loopCount = int(input())

stack = []

def push(putVal):
    stack.append(putVal)

def pop():
    try:
        print(stack.pop())
    except:
        print(-1)

def size():
    print(len(stack))

def empty():
    if len(stack) > 0:
        print(0)
    else:
        print(1)

def top():
    if len(stack) == 0:
        print(-1)
    else:
        print(stack[len(stack)-1])

for _ in range(loopCount):
    #inputData = input().split()        # 시간초과
    inputData = sys.stdin.readline().split()
    if inputData[0] == "push":
        push(inputData[1])
    elif inputData[0] == "pop":
        pop()
    elif inputData[0] == "size":
        size()
    elif inputData[0] == "empty":
        empty()
    elif inputData[0] == "top":
        top()