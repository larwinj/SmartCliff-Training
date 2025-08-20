# 9th code :

held = int(input("Enter number of classes held: "))
attended = int(input("Enter number of classes attended: "))

def func(held,attended):
  if held < attended:
    print("Invalid Input")
    return

  attendance = (attended / held) * 100

  if attendance >= 75:
    print("Allowed")
    print(f"{int(attendance)}%", end=" ")
  else:
    medical = input("Do you have a medical cause? (Y/N): ").strip().upper()
    print(f"{int(attendance)}%", end=" ")
    if medical == "Y":
      print("Allowed")
    else:
      print("Not allowed")

func(held,attended)