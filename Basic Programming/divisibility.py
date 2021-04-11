t= int(input())

l1= list(input().split())

for i in range(t):
    temp = l1[i][-1]

if(int(temp) %10 ==0):
    print("Yes")
else:
    print("No")
