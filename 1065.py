# #1065번 _ 한수
x = int(input(""))
answer = 0
while x:
    if x<100:
        answer += 1
        x -= 1
        continue
    if x == 1000:
        x -= 1
        continue
    y = len(str(x))
    numList = []
    for i in range(y):
        numList.append(str(x)[i])
    if int(numList[1])*2 == int(numList[0]) + int(numList[2]):
        answer += 1
    x -= 1
print(answer)