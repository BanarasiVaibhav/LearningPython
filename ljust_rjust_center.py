name=' kya karoge jaan kar '
sorry='I am sorry my name is Vaibhav'
print(' its alright '.join([name,sorry]))
print(name.split())
print(name.rjust(100,'-'))
print(name.ljust(100,'0'))
print(name.center(100,'*'))


# this is seperate piece of code
def printPicnic(itemsDict,leftWidth,rightWidth):
    print('PICNIC ITEMS'.center(leftWidth+rightWidth,'-'))
    for k,v in itemsDict.items():
        print(k.ljust(leftWidth,'-')+str(v.rjust(rightWidth,'~')))
picnicItems={'sandwiche':'6','maggi':'10','mat':'full size','camera':'190'}
printPicnic(picnicItems,18,18)
