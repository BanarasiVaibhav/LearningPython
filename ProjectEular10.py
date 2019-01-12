sum=0
for n in range(2,2000000):
    for i in range(2,int((n/2)+1)):
        if n%i==0:
            break
    else:
        sum=sum+n
        print(n)
print(sum)
