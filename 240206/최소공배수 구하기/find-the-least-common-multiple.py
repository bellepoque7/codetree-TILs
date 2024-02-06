import sys
read = sys.stdin.readline

n, m = map(int, read().split())
# 1. 한 수가 다른 수의 배수일 경우
# 큰 수가 최소 공배수이다.

# 2. 그렇지 않을 경우 
# 두 수를 동시에 나눌 수 있는 수를 찾은뒤 각 수를 최대공약수로 나누어 몫을 곱한다. 

k = max(n,m)
for i in range(2,100):
    if n%i ==0 and  m%i == 0:
        # print(i)
        k = i
print(n//k * m//k * k)