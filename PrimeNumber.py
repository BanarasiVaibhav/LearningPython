import math
print("2 is a prime number")
for i in range(3,1000,2):
  for j in range(2,int(math.sqrt(i))+1):
      if (i%j)==0:
        break
  else:
    print(str(i)+  " is a prime number")
