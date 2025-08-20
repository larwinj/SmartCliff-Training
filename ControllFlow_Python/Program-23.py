# 23th code :

num = input()

fl = True
for i in range(len(num) - 1):
    if abs(int(num[i]) - int(num[i+1])) != 1:
        fl = False
        break

if fl:
    print("YES")
else:
    print("NO")