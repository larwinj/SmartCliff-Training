# 27th Code :

def trap(hei):
  l, r = 0, len(hei) - 1

  # Concluding it with two pointer approach
  maxl, maxr = hei[l], hei[r]
  sol = 0
  while l < r:
    if hei[l] < hei[r]:
      sol += maxl - hei[l]
      l += 1
      maxl = max(maxl, hei[l])
    else:
      sol += maxr - hei[r]
      r -= 1
      maxr = max(maxr, hei[r])
  return sol

al = list(map(int,input().split()))
print(trap(al))