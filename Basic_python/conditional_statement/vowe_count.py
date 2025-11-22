word=input("Enter a word: ")
vowel_count=0   
for char in word:
    if char.lower()in "aeiou":
        vowel_count+=1
print("Number of vowels in the word:",vowel_count)