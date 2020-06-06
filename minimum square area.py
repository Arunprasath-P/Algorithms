t=int(input())
while(t):
    n=int(input())
    l1,l2=[],[]
    for i in range(n):
        a=list(map(int,input().split()))
        l1.append(a[0])
        l2.append(a[1])
    l1=sorted(l1)
    l2=sorted(l2)
    d=l1[n-1]-l1[0]
    e=l2[n-1]-l2[0]
    print(max(d,e)*max(d,e))
    t=t-1
