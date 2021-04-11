
# Write your code here

t= int(input())
nums = list(input().split())

h= t/2

new_num=[]

for i in range(t):
    if i<h:
        new_num.append(nums[i][0])
    else:
        new_num.append(nums[i][-1])

x= "".join(new_num)

if(int(x) %11 ==0):
    print("OUI")
else:
    print("NON")
