n,m=list(map(int,input().split(' ')))
l1=[]
for i in range(n):
    l1.append(input())
def creativestring(n,m):
    st1=""
    for i in range(n):
        st1+=input()
    for i in range(n--1,-1,-1):
        m-=i
        if(m>=0):
            if(m>=26):
                st1=st1[:i]+'z'+st1[i+1:]
                m-=26
            else:
                c=(m+97-1)
                st1=st1[:i]+chr(c)+st1[i+1:]
                m-=ord(st1[i])-ord('a')+1
        else:
            break
        m+=i
    return st1
print(creativestring(n,m))
            
    
