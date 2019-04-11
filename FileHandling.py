# program to append numbers 0 to 99 in a text file

import os
helloFile=open('C:\\Users\\Vaibhav Tiwari\\PYTHON.txt','a')
for i in range(0,100):
    helloFile.write(str(i))  #write numbers
    helloFile.write('\n')    #newline character

