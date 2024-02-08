n = int(input())

def get_squ(n):
    if n < 10:
        return n**2
    return get_squ(n//10) + (n%10)**2
print(get_squ(n))