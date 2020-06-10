l1=list(map(int,input().split()))
k=int(input())
l2=[]
for i in range(len(l1)):
    for j in range(len(l1)):
        if l1[i] * l1[j] < k and [j] not in l2:
            l2.append([j])
print(l2)    
