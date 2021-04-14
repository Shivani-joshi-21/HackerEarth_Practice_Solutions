# Write your code here
isbn = input()

add=0

if len(isbn) != 10:
   print("Illegal ISBN")
else:
    for i in range(1, 11):
        add += i * int(isbn[i-1])
    if add % 11 == 0:
      print("Legal ISBN")
    else:
      print("Illegal ISBN")
