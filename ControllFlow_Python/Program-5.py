# 5st code :

decimal_num = int(input())

binary_num = bin(decimal_num)[2:]   #Function to find the binary numbers
octal_num = oct(decimal_num)[2:]    #Function to find the Octal
hexadecimal_num = hex(decimal_num)[2:].upper()   #Function to find the hexadecimal

print("Binary:", binary_num)
print("Octal:", octal_num)
print("Hexadecimal:", hexadecimal_num)