import sys
read = sys.stdin.readline

n, m = map(int, read().split())

#최대 공약수 변수 초기화
k = 0

# 100까지 루프 돌려서 최대공약수를 찾으면 할당
for i in range(2,100):
    if n%i ==0 and  m%i == 0:
        # print(i)
        k = i
# 최대 공약수가 없다면 서로소. 두수 곱하여 최소공배수 출력
if k == 0 :
    print(n*m)
else:
    print(n//k * m//k * k)