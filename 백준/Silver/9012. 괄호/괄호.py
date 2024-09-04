import sys
T = int(sys.stdin.readline().strip())

for i in range(T):
    string = sys.stdin.readline().strip()
    left_list = []
    need_left = 0
    result = True
    for s in list(string):
        if s == '(':
            left_list.append(s)
        else:
            if(len(left_list) > 0):
                left_list.pop(-1)
            else:
                result = False
                break
    if result == True and len(left_list) == 0:
        print("YES")
    else:
        print("NO")