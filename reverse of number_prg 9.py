def reverse_number(num):
    rev = 0
    while num:
        rev = rev * 10 + num % 10
        num //= 10 #removes  last digit
    return rev

num = int(input("Enter a number with at least 4 digits: "))
while len(str(num)) < 4:
    num = int(input("Please enter at least 4 digits: "))

print("Original Number:", num)
print("Reversed Number:", reverse_number(num))
