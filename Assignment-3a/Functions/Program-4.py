from num2words import num2words

# Converted using this num2words package
def number_to_words(num):
    return num2words(num)

s = input("Enter the elements: ")
print(number_to_words(s))