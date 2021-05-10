import sys

loop = int(input())

for _ in range(loop):
    many, idx = map(int, sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().split()))

    watch = idx                 # 내가 알고싶은 대상
    count = 0
    while True:
        maxPri = max(arr)       # 제일 높은 우선순위값 가져오기
        if arr[0] >= maxPri:
            count+=1            # 출력 순서 카운트
            if watch == 0:      # 내가 알고싶은 대상이 현재 출력되는지
                print(count)    # 몇번째 순서에 카운트 됫는지 출력
                break
            else:
                arr.pop(0)      # 단순 추출 후 삭제
        else:
            arr.append(arr.pop(0))  # 우선순위가 높지않기에 뒤로가!

        if 0 == watch:          # 내가 알고싶은 대상의 위치가 바뀌기에 변경
            watch = len(arr)-1
        else:
            watch -= 1