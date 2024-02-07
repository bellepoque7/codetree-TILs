import sys

n = int(input())

def get_hello(n):
    print('HelloWorld')
    if n == 1:
        return
    get_hello(n-1)
get_hello(n)