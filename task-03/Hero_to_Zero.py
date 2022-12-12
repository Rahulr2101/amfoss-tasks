cities = int(input())
for count1 in range(cities):
    count = 0
    hero_number = int(input())
    hero_level = list(map(int,input().split()))
    hero_level.sort()
    for count1 in hero_level:
        if count1 != 0:
            if hero_level.count(count1)>1:
                find_ind = hero_level.index(count1)
                hero_level[find_ind] = 0
                count += 1

        

    for null in range(100):
        if max(hero_level) != 0:
            hero_level.sort()
            if hero_level[0] == 0:
           
                max_num_idx = hero_level.index(max(hero_level))
                hero_level[max_num_idx] = 0
                count += 1
            else:
                        hero_level[hero_number-1] = min(hero_level)
                        hero_level[hero_number-1] = 0
                        hero_level.sort()
                        count +=2
        else :
            print(count)
            break

