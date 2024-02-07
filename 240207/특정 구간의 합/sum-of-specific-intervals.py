import sys

read = sys.stdin.readline
n,m = map(int, read().split())
my_list = list(map(int, input().split()))

for i in range(m):
    s,e = map(int, read().split())
    print(sum(my_list[s-1:e]))