import sys

read = sys.stdin.readline
Y, M, D = map(int, read().split())

#31일이 있는 월
# 1,3,5,7,8,10,12

#30일 까지 있는 월
#4,6,9,11

#2월은 28일까지 
# 단 4의 배수면 29일까지
# 단 4의 배수면서 100의 배수면 28일까지
# 단 4의 배수이서 100의 배수지만 400의 배수이면 29일까지
# 나머지는 29일까지
# Y, M, D = 1999, 2, 29

Month = ''
Flag = False
#월체크
if  M in (3,4,5):
    Month = 'Spring'
elif M in (6,7,8):
    Month = 'Summer'
elif M in (9,10,11):
    Month = 'Fall'
elif M in (1,2,12):
    Month = 'Winter'

# 존재하는 날짜인지 체크
if M in (1,3,5,7,8,10,12):
    if 1<= D <= 31:
        Flag = True
    else:
        pass
elif M in (4,6,9,11):
    if 1<= D <= 30:
        Flag = True
    else:
        pass
elif M == 2:
    if Y%4 ==0 and Y%100 == 0 and Y%400 == 0 and 1<= D <= 29:
        Flag = True
    elif Y% 4 ==0 and Y%100 == 0 and 1<= D <= 28:
        Flag = True
    elif Y% 4 ==0 and 1<=D <=29:
        Flag = True
    elif Y% 4 !=0 and 1<= D <= 28:
        Flag = True
    else:
        pass
else:
    pass


if Flag:
    print(Month)
else:
    print(-1)