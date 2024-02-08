n = int(input())
n = 10

def get_fact(n):
    if n == 1:
        return 1
    return n + get_fact(n-1)
    

print(get_fact(n))