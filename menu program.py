while True:
    print("MENU PROGRAM:")
    print(" 1. Occurence of word\n 2. Charecter Frequency\n 3. Factors of a given number\n 4. EXIT")
    choice=int(input("Enter your choice:"))
    if choice > 4 or choice < 1:
        print("Your choice is not in the list")
    
    elif choice == 1:
        text = input("Enter text: ")
        words = text.split()
        count = {}
        for w in words:
            count[w] = count.get(w, 0) + 1
        print(count)
        print("\n")
    elif choice == 2:
        text=input("Enter a word:")
        count = {}
        for ch in text:
            count[ch] = count.get(ch, 0) + 1
        print(count)
        print("\n")
    elif choice == 3:
        a=int(input("Enter the number:"))   
        for i in range(1, a+1):
            if a % i == 0:
             print(i," ")
    else:
        print("Exit")
        break
