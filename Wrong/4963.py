import sys
sys.setrecursionlimit(10000000)
# DFS 메서드 정의
def dfs(x, y):
  if x <= -1 or x >= M or y <= -1 or y >= N:
    return False
  if graph[x][y] == 1:
    graph[x][y] = 3
    dfs(x-1,y)
    dfs(x,y-1)
    dfs(x+1,y)
    dfs(x,y+1)
    dfs(x+1,y+1)
    dfs(x+1,y-1)
    dfs(x-1,y+1)
    dfs(x-1,y-1)
    return True
  return False

while True:
  N, M = map(int,input().split(" "))
  graph = []
  for i in range(M):
    graph.append(list(map(int,input().split(" "))))
  result = 0
  if N+M == 0:
    break
  for i in range(N):
    for j in range(M):
      if dfs(i,j) == True:
        result += 1
  print(result)

## 케이스는 다 맞는데 진짜 왜 틀렸는지 모르겠다 ,, 런타임 오류!!!!!!!!!!!!!!
