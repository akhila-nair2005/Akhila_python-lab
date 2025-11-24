word=input("Enter a string:")
x=word[0]
print(x)
for ch in word[1:]:
    if(ch==x):
        print(ch.replace(ch,"$"))
    else:
        print(ch)
    
