import sys

queue = []

def push(val):
    queue.append(val)

def pop():
    try:
        return print(queue.pop(0))
    except:
        return print(-1)

def size():
    return print(len(queue))

def empty():
    return print(1 if len(queue) == 0 else 0)

def front():
    if len(queue) > 0:
        return print(queue[0])
    else:
        return print(-1)

def back():
    if len(queue) > 0:
        return print(queue[len(queue)-1])
    else:
        return print(-1)


loop = int(input())
for _ in range(loop):
    input = list(sys.stdin.readline().split())
    if input[0] == "push":
        push(input[1])
    elif input[0] == "pop":
        pop()
    elif input[0] == "size":
        size()
    elif input[0] == "empty":
        empty()
    elif input[0] == "front":
        front()
    elif input[0] == "back":
        back()
    else:
        print(-1)