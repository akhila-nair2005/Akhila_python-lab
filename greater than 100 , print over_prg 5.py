#prompt the user for a list of inmtegers for all values greater than 100, store "over" instead..

num=int(input("Enter numbers:"))
for i in num:
    if i>100:
        print("over")
    else:
        print(i)
