a,b=input().split()
a=int(a)
b=int(b)

c=a%4
d=b%4
 
if c==0 and d==0:
    for a in range(a,b,4):
        print(a)
       
else:
    print(-1)

