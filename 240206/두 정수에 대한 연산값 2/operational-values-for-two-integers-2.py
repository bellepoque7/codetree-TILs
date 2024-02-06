import sys
a, b = map(int, sys.stdin.readline().split())

if a > b:
    a  = a*2
    b = b+10
else:
    b = b*2
    a = a + 10
print(a,b)