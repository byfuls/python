length = int(input())
content = [s for s in input()]

print(length)
print(content)

jump = 2
skip = False
newContent = []
for idx in range(1, length, 2):
    if skip is True:
        skip = False
        continue

    if content[idx] == "+":
        if content[idx+jump] == "+":
            if content[idx-1] > content[idx+jump+1]:
                newContent.append(str(content[idx-1]+content[idx+1]))
                newContent.append(content[idx])
                newContent.append(content[idx+jump+1])
            else:
                newContent.append(str(content[idx-1]))
                newContent.append(content[idx])
                newContent.append(str(content[idx+jump+1]+content[idx+1]))
            skip = True
        else:
            newContent.append(str(content[idx-1]+content[idx+1]))
    elif content[idx] == "*":
        