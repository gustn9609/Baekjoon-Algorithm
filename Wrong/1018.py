# #1018번 _ 체스판 다시 칠하기
N, M = int(input(""))

for i in range(N):
    globals()["row"+str(i)] = input("")

start_num = M-8

answer_list = []
for i in range(N):
    for j in range(start_num):
        if ["row"+"i"][j] != ["row"+"i"][j+1]:
            answer += 1

    answer = 0

# 피드백
# 2차원 데이터를 리스트로 받아서 for문을 두번 사용하는게 아직 어색한것 같다!