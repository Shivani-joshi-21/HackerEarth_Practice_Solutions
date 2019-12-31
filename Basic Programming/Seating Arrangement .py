# Write your code here
no_of_test_cases=int(input())
seat_nos=[]
rem=0
while(no_of_test_cases):
    seat_nos.append(int(input()))
    no_of_test_cases-=1
for i in range(len(seat_nos)):
    rem= seat_nos[i]%12
    if rem ==1:
        print(seat_nos[i]+11 ,'WS')
    elif rem==0:
        print(seat_nos[i]-11,'WS')
    elif rem==6:
        print(seat_nos[i]+1 ,'WS')
    elif rem==7:
         print(seat_nos[i]-1 ,'WS')
    elif rem==2:
        print(seat_nos[i]+9,'MS')
    elif rem==11:
        print(seat_nos[i]-9,'MS')
    elif rem==5:
        print(seat_nos[i]+3,'MS')
    elif rem==8:
        print(seat_nos[i]-3,'MS')
    elif rem==3:
         print(seat_nos[i]+7,'AS')
    elif rem==10:
         print(seat_nos[i]-7,'AS')
    elif rem==4:
         print(seat_nos[i]+5,'AS')
    elif rem==9:
         print(seat_nos[i]-5,'AS')
    rem=0
