# Write your code here
n= int(input())

if(n%5==0):
    steps = n//5
else:
    steps = n//5 + 1
print(steps)
