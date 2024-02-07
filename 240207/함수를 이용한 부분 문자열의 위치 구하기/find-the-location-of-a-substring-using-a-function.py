ipt_str = input()
obj_str = input()
Flag = False
idx = -1
#tadada
#da

for i in range(len(ipt_str)):
    if Flag:
        break
    for j in range(len(obj_str)):
        if ipt_str[i: i+len(ipt_str)] == obj_str:
            idx = i
            Flag = True
            break
    
print(idx)