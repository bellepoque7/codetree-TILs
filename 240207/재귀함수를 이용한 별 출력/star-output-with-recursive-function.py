n = int(input())

def get_star(n):
    if n == 0:
        return
    get_star(n-1)
    print('*'*n)
get_star(n)