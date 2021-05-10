n = int(input())

stack = [i for i in range(1, n+1)]

while len(stack) > 1:
    print(stack)
    stack.pop(0)
    print(stack)
    stack.append(stack.pop(0))
    print(stack)

print(stack.pop())
# pop()을 두번써서 시간초과 인건가..?

#from collections import deque
#n = int(input())
#
#deq = deque([i for i in range(1, n+1)])
#while len(deq) > 1:
#    deq.popleft()
#    deq.append(deq.popleft())
#print(deq.pop())