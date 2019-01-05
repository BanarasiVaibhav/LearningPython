import sys
number=int(input("Enter any number to check collatz conjucture :"))

def collatz(number):
  if number==1:
    sys.exit()

  if number%2==0:
    number=number/2
    print(number)
    collatz(number)
  elif number%2!=0:
    number=3*number+1
    print(number)
    collatz(number)
print("No matter what is the number the sequence always reaches 1")
collatz(number)
