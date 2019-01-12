def factorial(num):
    for i in range(1,num+1):
        num=num*i
    return num
print(factorial(100))

digits=factorial(100)
length=list(str(digits))
sum=0
for j in range(1,len(length)+1):
    sum=sum+digits%10
    digits=digits//10
print(sum)
