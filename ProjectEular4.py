#project Eular 4
array=[]
lis=[]
for n in range(998001,10000,-1):
    a=n

    x=int(n/1000)

    p=a%10
    a=int(a/10)

    q=a%10
    a = int(a / 10)

    r=a%10
    a = int(a / 10)

    if x==p*100+q*10+r:
        array=array+[n]

for i in range(999,100,-1):
    for j in range(999,100,-1):
        for k in range(0,len(array)-1):
            if array[k]==i*j:
                lis=lis+[array[k]]
                print(max(lis))
