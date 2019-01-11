I have no Idea how & why my code works
 All i know that somehow it works 


Language used Python 3


array=[]
if len(array)<10001:
	for num in range(1,1000100):
		for i in range(2,num):
			if (num%i)==0:
				break
		else:
			print(num)
			array=array+[num]
print(array[10001])


if you are reading this please help me to optimize this code 
it took about an hour to print solution  
