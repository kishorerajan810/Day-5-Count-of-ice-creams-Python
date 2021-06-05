a,b=map(int,input("enter:").split())
c=input("Enter:").split()
c.sort(key=int)
d=0
count=0
for i in c:
    d=d+int(i)
    if d<=b:
        count+=1
print(count)
    
