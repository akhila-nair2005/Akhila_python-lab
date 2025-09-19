#Greatest of 3 number

print("GREATEST OF 3 NUMBER\n")

a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
c=int(input("Enter the third number:"))

if a>b & a>c:
      print(a,"is greater")
elif b>c:
      print(b,"is greater")
else:
      print(c,"is greater")
