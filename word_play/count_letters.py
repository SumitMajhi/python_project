sentence = str(input("Enter your statement: "))

upper = lower = const = vowels = special = 0

vowels_set = set("aeiouAEIOU")
special_set = set("!@#$%^&*()_+-=[]{}|;:'\",.<>?/")

for c in sentence:
    if c.isupper():
        upper += 1
    elif c.islower():
        lower += 1

    if c in vowels_set:
        vowels += 1
    elif c in special_set:
        special += 1
    elif c.isalpha() and c not in vowels_set:
        const += 1

total_characters = len(sentence)

print(f"Uppercase letters = {upper}")
print(f"Lowercase letters = {lower}")
print(f"Vowels = {vowels}")
print(f"Consonants = {const}")
print(f"Special characters = {special}")
print(f"Total characters = {total_characters}") 
