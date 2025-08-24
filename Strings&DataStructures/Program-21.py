s = input()

sml = 0
lrg = 0
otr = 0

for i in s:
    if i.islower():
        sml += 1
    elif i.isupper():
        lrg += 1
    else:
        otr += 1

print("Lower case letters",sml)
print("Upper case letters",lrg)
print("Non - letters",otr)