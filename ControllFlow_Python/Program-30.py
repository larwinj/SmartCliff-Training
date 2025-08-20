# 30th Code :

def drm(n):
    while n >= 10:
        p = 1
        for i in str(n):
            p *= int(i)
        n = p
    return n

print(drm(int(input())))