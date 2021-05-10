count, num = map(int, input().split())

josephus = [i for i in range(1, count+1)]

result = []
seqNo = num-1
while len(josephus):
    if seqNo >= len(josephus):
        #seqNo = seqNo - len(josephus)  얘두 댐!
        seqNo = seqNo % len(josephus)
    else:
        result.append(str(josephus.pop(seqNo)))
        seqNo += (num-1)

print("<", ", ".join(result), ">", sep='')