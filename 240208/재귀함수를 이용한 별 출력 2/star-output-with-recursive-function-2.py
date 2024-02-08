n = int(input())

def get_num(n):
    if n ==0:
        return 
    print('* '*n)
    get_num(n-1)
    print('* '*n)
get_num(n)