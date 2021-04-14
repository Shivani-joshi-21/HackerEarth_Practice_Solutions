# Write your code here
n = int(input())
l1 = list(map(int,input().split()))
l2 = sorted(l1)
k=-1
add = sum(l1)
for i in range(n):
    z = add-l2[i]
    if z%7==0:
        k = l2[i]
        break
if k!=-1:
    print(l1.index(k))
else:
    print(k)
