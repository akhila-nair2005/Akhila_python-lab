#Form a list of vowels selected from a given world

word = (input("Enter a text: "))
vowels = 'aeiouAEIOU'
i = 0
result = []

while i < len(word):
    if word[i] in vowels:
        result += word[i]  # using += instead of append
    i += 1

print("Vowels:", result)

