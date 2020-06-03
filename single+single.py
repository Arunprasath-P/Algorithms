n=int(input())
while(n):
    val=input()
    if len(val) == len(set(val)):
        print("No")
    else:
        print("Yes")
    '''for i in val:
        if val.count(i)%2 == 0:
            print("Yes")
            break
    else:
        print("No")'''
    n=n-1
    
