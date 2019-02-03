'''This is a multi line comment
this code checks if the age entered is valid or not
valid in the sense it should only contain numbers as 56.5 and not fifty six'''

#enter your age verification
while True:
  age=input("Enter your age :  ")
  if age.isdecimal():
    break
  print("enter your age in decimal")

'''This is a multi line comment
this code checks if the email entered is valid or not
valid in the sense it should only contain alphanumeric and no space should contain pfrase '.com' and be in lower case'''


# email checking
while True:
  email=input("Enter your email:  ")
  if email.islower():
    if '.com' in email:
      if email.isalnum():
        break
  print("enter valid email")
