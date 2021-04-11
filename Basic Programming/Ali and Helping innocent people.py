s=input()
flag = 0
v = ['A','E','I','O','U','Y']
if((int(s[0])+int(s[1]))%2==1):
    flag = 1
if((int(s[3])+int(s[4]))%2==1):
    flag = 1
if((int(s[4])+int(s[5]))%2==1):
    flag = 1
if((int(s[7])+int(s[8]))%2==1):
    flag = 1
if s[2] in v:
    flag = 1
if(flag==0):
    print('valid')
else:
    print('invalid')
