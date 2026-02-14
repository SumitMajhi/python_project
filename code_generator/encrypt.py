import string 
import random

def code_word(msg, key):
    raw = msg.split()
    lst = []

    for word in raw:
        if len(word) < 3 :
            encrypt = word[::-1]
            lst.append(encrypt)
        else:
            code = word[1:] + word[0]
            prefix = ''.join(random.choices(string.ascii_lowercase, k=key))
            suffix = ''.join(random.choices(string.ascii_lowercase, k=key))
            encrypted = prefix + code + suffix
            lst.append(encrypted)
    encrypt = ' '.join(lst)
    return encrypt
    
def code_word_decrypt(msg,key):
    raw = msg.split()
    lst = []

    for word in raw:
        if len(word) < (key * 2 + 2) :
            lst.append(word[::-1])
        else:
            code = word[key:-key]
            decoded = code[-1] + code[:-1]
            lst.append(decoded)
    encrypt = ' '.join(lst)
    return encrypt

while True:
    action = input("Enter operation number (1. Encrypt, 2. Decrypt, 3. Exit) : ")
    if action == '1':
        message = input("Enter message to Encrypt : ")
        try:
            pass_key = int(input("Enter random number to encrypt : "))
            print("Encrypted Message : ", code_word(message, pass_key))
        except ValueError:
            print("Please enter a valid number.")

    elif action == '2':
        message = input("Enter message to decrypt: ")
        try:
            pass_key = int(input("Enter the key used to encrypt: "))
            print("Decrypted Message : ", code_word_decrypt(message, pass_key))
        except ValueError:
            print("Please enter a valid number.")

    elif action == '3':
        print("Exiting the program.")
        break
    else:
        print("Invalid operation number. Please try again.")
