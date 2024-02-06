import sys

n = int(input())
read = sys.stdin.readline
my_list = list(map(int, read().split()))

for i in my_list:
    if i % 2 == 0:
        print(i//2, end =' ')
    else:
        print(i, end =' ')