# Write your code here
days= int(input())
toffees=0
while(days>0):
    days-=1
    radius,horlicks=map(int,input().split())  
    c = 2*22/7*radius
    dist = 100 * horlicks
    if dist>=c:
        toffees+=1
print (toffees)
