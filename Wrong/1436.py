# #1436번 _ 영화감독 숌
# left + 666 + right
n = int(input(""))
left = 0
right = 0
if n<6:
    left = n-1
    answer = int(str(left)+"666")
else:
    MM = (n-7) // 19
    NN = (n-7) % 19
    print(MM,NN)
    if n < 19 * MM + 17:
        left = MM
        right = NN
    else:
        left = 0
        right = MM*10 + 7
    answer = int(str(left)+"666"+str(right))
print(answer)

# 666 => 666347 34 13
#        256664
# def movie_title(n):
#     i = 0
#     cnt = 0
#     while True:
#         i += 1
#         j = str(i)
#         if j.count("666") >= 1:
#             title = i
#             cnt += 1
#         if cnt == n:
#             break
#     print(title)
#     return title

# n = int(input())
# movie_title(n)

# 왜 틀렸나?
# n번째 항의 일반항을 구하는 풀이가 아닌 1번째부터 차례대로 찾는 '탐색'느낌으로 풀자!
# int값 안에 어떤 수가 포함되어 있는지는 str로 바꾼 후 j.count("666")과 같이 나타낼 수 있다.