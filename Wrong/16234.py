from collections import deque
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y,cnt):
    queue = deque()
    queue.append((x,y))
    print(queue)

    while queue:
        print("몇번반복할까")
        x,y = queue.popleft()
        dongmang_list = [[x,y]]
        dongmang_cnt = 1
        dongmang_people = lst[x][y]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            print(nx,ny)
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if a <= abs(lst[x][y] - lst[nx][ny]) <= b:
                dongmang_list.append([nx,ny])
                dongmang_cnt += 1
                dongmang_people += lst[nx][ny]
                queue.append((nx,ny))
                print(dongmang_list,dongmang_cnt,dongmang_people)
            cnt+=1
        for ll in dongmang_list:
            print(ll)
            lst[ll[0]][ll[1]] = dongmang_people/dongmang_cnt
            print("찐",lst)

n, a, b = map(int, input().split())
lst = []
cnt = 0
for i in range(n):
    lst.append(list(map(int, input().split())))
for x in range(n):
    print("x","--------------",x,"--------------")
    for y in range(n):
        print("y","--------------",y,"--------------")
        bfs(x, y,cnt)
        print(cnt)
