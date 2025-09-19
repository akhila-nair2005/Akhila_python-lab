#Count the occurences of each word in a line of text

print("REPETITION OF WORD IN A LINE OF TEXT\n")

text = input("Enter text: ")
words = text.split()

count = {}

for w in words:
    count[w] = count.get(w, 0) + 1

print(count)
