import sys

loopCount = int(input())

stack = []

def push(putVal):
    stack.append(putVal)        # stack(list) 맨 뒤에 항목 추가

def pop():
    try:
        return stack.pop()      # stack(list) 맨 뒤에 항목 추출 및 삭제
    except:
        return -1

def size():
    return len(stack)           # stack(list) 항목 개수 출력

def empty():
    if len(stack) > 0:
        return 0
    else:
        return 1

def top():
    if len(stack) == 0:
        return -1
    else:
        return stack[len(stack)-1]  # stack(list) 항목의 맨 끝 항목 출력

for _ in range(loopCount):
    #inputData = input().split()                # 시간초과
    inputData = sys.stdin.readline().split()    # for 문 안에서는 sys.stdin 으로 활용
    if inputData[0] == "push":
        push(inputData[1])
    elif inputData[0] == "pop":
        print(pop())
    elif inputData[0] == "size":
        print(size())
    elif inputData[0] == "empty":
        print(empty())
    elif inputData[0] == "top":
        print(top())