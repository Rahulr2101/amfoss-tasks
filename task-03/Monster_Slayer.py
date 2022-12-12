testcase = int(input())
a = True
b = False
for x in range(testcase):
    number_grp = int(input())
    grp_list = list(map(int,input().split()))
    for y in range(len(grp_list)):
        if b:
            break
        for z in grp_list:
            d = grp_list[0]
            if z%d != 0:
                a = False
                b = True
                print("NO")
                break
    if a:        
        print("YES")

