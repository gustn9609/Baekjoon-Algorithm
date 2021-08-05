# #14501번 _ 퇴사

N = int(input(""))
alist = []
for i in range(N):
    x,y = input("").split(" ")
    alist.append([x,y])
# N=7
# list = [[3,10],[5,20],[1,10], [1,20], [2,15], [4,40],[2,200]]
money_list = []
for i in range(1,N+1):
    canday = i
    money = 0
    while canday<=N:
        if int(canday+int(alist[canday-1][0]))>N:
            break
        money += int(alist[canday-1][1])
        canday += int(alist[canday-1][0])
    money_list.append(money)
print(money_list)

# 풀이1
# 뒤에서부터 풀 생각 ,, 하기!
# n = int(input())
# t = []
# p = []
# dp = []
# for i in range(n):
#     a, b = map(int, input().split())
#     t.append(a)
#     p.append(b)
#     dp.append(b)
# dp.append(0)
# for i in range(n - 1, -1, -1):
#     if t[i] + i > n:
#         dp[i] = dp[i + 1]
#     else:
#         dp[i] = max(dp[i + 1], p[i] + dp[i + t[i]])
# print(dp[0])

# 풀이2
# 다이나믹 프로그래밍 좀 더 공부하자!
# N번째 날은 N+1번째 날 기준 수익(dp)과 N번째 날 수익 + Tn 만큼 지난 후 수익(dp)중 큰 값을 골라야한다.
# import sys

# N = int(input())

# timeTable = [list(map(int,sys.stdin.readline().split())) for i in range(N)]

# dp = [0 for i in range(N+1)]

# for i in range(N-1,-1,-1):
#     if i + timeTable[i][0] > N:
#         dp[i] = dp[i+1]
#     else:
#         dp[i] = max(timeTable[i][1] + dp[i + timeTable[i][0]], dp[i+1])

# print(dp[0])