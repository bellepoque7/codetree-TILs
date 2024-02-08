n = int(input())
def get_num(n, cnt):
    if n == 1:
        return cnt
    if n % 2 == 0:
        cnt += 1
        return get_num(n//2, cnt)
    else:
        cnt += 1
        return get_num(n//3, cnt)

print(get_num(n, 0))