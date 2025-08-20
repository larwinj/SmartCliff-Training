# 12th code :

amt = int(input())

if amt % 500 != 0:
    print("please enter the amount multiple of 500")
else:
    if amt == 500:
        print("5 notes of 100")
    elif amt <= 2000:
        hundreds = 5
        five_hundreds = (amt - 500) // 500
        print(f"{hundreds} notes of 100 & {five_hundreds} notes of 500")
    else:
        hundreds = 5
        remaining = amt - 500

        two_thousands = remaining // 2000
        remaining = (amt-500) - (two_thousands * 2000)
        five_hundreds = 0

        if remaining >= 500:
            five_hundreds = (remaining) // 500
        if five_hundreds == 0:
          print(f"{hundreds} notes of 100 && {two_thousands} notes of 2000")
        elif two_thousands == 0:
          print(f"{hundreds} notes of 100 && {five_hundreds} notes of 500")
        else:
          print(f"{hundreds} notes of 100, {two_thousands} notes of 2000, {five_hundreds} notes of 500")