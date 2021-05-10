import sys

deque = []

def push_front(val):
    deque.insert(0, val)

def push_back(val):
    deque.append(val)

def pop_front():
    try:
        return deque.pop(0)
    except:
        return -1

def pop_back():
    try:
        return deque.pop()
    except:
        return -1

def size():
    return len(deque)

def empty():
    return 1 if len(deque) == 0 else 0

def front():
    return -1 if len(deque) == 0 else deque[0]

def back():
    return -1 if len(deque) == 0 else deque[len(deque)-1]

loop = int(input())
for _ in range(loop):
    cmd = list(sys.stdin.readline().split())
    if cmd[0] == "push_front" : push_front(cmd[1])
    elif cmd[0] == "push_back": push_back(cmd[1])
    elif cmd[0] == "pop_front": print(pop_front())
    elif cmd[0] == "pop_back" : print(pop_back())
    elif cmd[0] == "size"     : print(size())
    elif cmd[0] == "empty"    : print(empty())
    elif cmd[0] == "front"    : print(front())
    elif cmd[0] == "back"     : print(back())
    else:
        print(-1)
