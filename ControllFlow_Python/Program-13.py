# 13th code :

num1 = int(input())
num2 = int(input())

cnt = 1;
# Making flag values for indicating the ding and dong
fl = False

for i in range(num1,num2+1):
  if cnt == 5:
    if fl == False:
      print("ding",end = " ")
      fl = True
    else:
      print("dong",end = " ")
      fl = False
    cnt = 1
    continue

  print(i,end=" ")
  cnt+=1