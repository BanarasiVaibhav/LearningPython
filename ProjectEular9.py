import sys
for c in range(1,999):
    for b in range(1,c):
        for a in range(1,b):
            if a*a+b*b==c*c:
                if a+b+c==1000:
                    print(a*b*c)
                    sys.exit()
