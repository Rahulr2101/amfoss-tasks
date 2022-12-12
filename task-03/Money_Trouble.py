z = list(map(int,input().split()))
n = z[0]
m = z[1]
if n<m:
    print(-1)
else:
    
        note_no =[]

        if n%2==0:
            for null in range(int((n/2)),n+1):
                note_no.append(null)
        else:
            for null in range(int((n-1)/2),n+1):
                note_no.append(null)
       

  
        for null in range(len(note_no)):
            if min(note_no)%m ==0:
                print(min(note_no))
                break

            elif min(note_no)!=0:
                note_no.remove(min(note_no))
              
            else:
                print(-1)


