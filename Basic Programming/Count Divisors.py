# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''
 
# Write your code here
nums= input().split()
count=0
l =int(nums[0])
r= int(nums[1])
k= int(nums[2])
for i in range(l,r+1):
    if(i%k==0):
        count+=1
print (count)
