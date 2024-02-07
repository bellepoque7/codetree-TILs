ipt_str = input()
obj_str = input()
Flag = False
idx = -1
for i in range(len(ipt_str)):
    for j in range(len(obj_str)):
        if ipt_str[i: i+len(obj_str)] == obj_str:
            idx = i
            Flag = True
            break
    if Flag:
        break
print(idx)