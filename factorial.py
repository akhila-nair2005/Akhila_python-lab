print("FACTORIAL OF A NUMBER\n")

num=int(input("Enter a number:"))
factorial=1
if num==0:
    print("the factorial of 0 is 1")
else:
    for i in range(1,num+1):
        factorial*=i
    print("Factorial is",factorial)
