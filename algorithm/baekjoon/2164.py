n = int(input())

stack = [i for i in range(1, n+1)]

#while len(stack) > 1:
#    print(stack)
#    stack.pop(0)
#    print(stack)
#    stack.append(stack.pop(0))
#    print(stack)
#
#print(stack.pop())
# ERROR(시간초과) => pop()을 두번써서 시간초과 인건가..

from collections import deque
n = int(input())

deq = deque([i for i in range(1, n+1)])
while len(deq) > 1:
    deq.popleft()               # 제일 왼쪽값 추출 및 삭제
    deq.append(deq.popleft())   # 맨 끝에 값 추가
print(deq.pop())                # 값 추출 및 삭제