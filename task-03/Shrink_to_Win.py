def rep(new_sum,number,count):
    if len(str(number)) != 1:
        for num in str(number):
            new_sum += int(num)
        count += 1
        if len(str(new_sum))>1:
            rep(0,int(new_sum),count)
        else:
            print(count)
    else :
        print(count)


number = input()
new_sum = 0
count =0
rep(new_sum,number,count)

