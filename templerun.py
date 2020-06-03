n=int(input())
l1=list(map(int,input().split()))
m=int(input())
for i in range(m):
    s=0
    val=int(input())
    if sum(l1)<val:
        print(-1)
        s=0
    else:
        for j in range(n):
            s=s+l1[j]
            if s>=val:
                print(j+1)
                s=0
                break
    
