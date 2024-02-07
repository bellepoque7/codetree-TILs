import sys
read = sys.stdin.readline
n, m = map(int, read().split())
my_list = list(map(int, input().split()))
my_sum = 0
for i in range(n):
    my_sum += my_list[m-1]
    if m == 1:
        break
    if m % 2 == 0 :
        m = m//2
    else:
        m -= 1
print(my_sum)