import re #import regular expression module https://docs.python.org/3/library/re.html

message='''Hello my name is vaibhav i am vaibhav my real name is also vaibhav my friende call me vaibhav'''

print(re.finditer(r'vaibhav',message))         # finditer
print(re.search(r'vaibhav',message))           #searches all over string
print(re.match(r'vaibhav',message))            #matches pattern only at begining
print(re.findall(r'vaibhav',message))          # find all returns list
