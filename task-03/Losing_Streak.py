a = list(map(int,input().split()))
target = a[0]
amount = a[1]
sm = amount
q = 1
count = 0
if amount % target == 0:
    while amount != target:
        while amount !=target:
            if q == 1:
                sm = sm/3
                if sm%target != 0:
                    q = 2
                    sm = amount
                    break
                count += 1
                amount = sm
            elif q == 2:
                sm =  sm/2
                if sm%target !=0:
                    q = 1
                    sm = amount
                    break
                count += 1
                amount = sm 
    print(count)
else:
    print(-1)


