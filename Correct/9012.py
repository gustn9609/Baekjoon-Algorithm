N = int(input(""))
for i in range(N):
    list = ""
    ps = input("")
    for i in range(len(ps)):
        list += ps[i]
        if "()" in list:
            list = list.replace("()","")
    if list:
        print("NO")
    else:
        print("YES")