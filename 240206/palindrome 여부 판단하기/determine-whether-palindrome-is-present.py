my_str = input()


# my_str = 'abcba'
n = len(my_str)
Flag = True
for i in range(n//2):
    if my_str[i] == my_str[-i -1]:
        pass
    else:
        Flag = False

if Flag:
    print('Yes')
else:
    print('No')