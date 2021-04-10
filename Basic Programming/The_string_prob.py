T = int(input())
while(T):
    strng = set(str(input()))
    vowels_1 = set('AEIOU')
    vowels_2 = set('aeiou')
    if vowels_1.issubset(strng):
        print('lovely string')
    elif vowels_2.issubset(strng):
        print('lovely string')
    else:
        print('ugly string')
    T -= 1
