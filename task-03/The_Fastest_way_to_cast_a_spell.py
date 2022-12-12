lenght = list(map(int,input().split()))
num = lenght[1]
count =0
word_dic ={

}
for null1 in range(num):
    a = input().split()
    for word in a:
        for word2 in a:
            minv = word
            
            if len(minv)>len(word2):
                minv = word2
                x = word2
                
    for word3 in a:
        word_dic[word3] = x
sen = input().split()
for sen1 in sen:
    a =word_dic[sen1]
    sen[count] = a
    count += 1
print(' '.join(sen))


