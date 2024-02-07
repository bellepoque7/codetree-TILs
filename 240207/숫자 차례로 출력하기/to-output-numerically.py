n = int(input())

def get_num(n):
    if n == 0:
        return 
    
    get_num(n-1)
    print(n, end = ' ')

def get_num2(n):
    if n == 0:
        return 
    print(n, end = ' ')
    get_num2(n-1)
get_num(n)
print()
get_num2(n)