# Secret Code Generator using Caesar Cipher

def encode_message(message, shift):
    encoded = ""
    for char in message:
        if char.isalpha():  # Only shift alphabet characters
            ascii_start = ord('A') if char.isupper() else ord('a')
            # Shift character and wrap around using modulo
            shifted = (ord(char) - ascii_start + shift) % 26 + ascii_start
            encoded += chr(shifted)
        else:
            encoded += char  # Leave non-letter characters unchanged
    return encoded


def decode_message(message, shift):
    # Decoding is encoding with negative shift
    return encode_message(message, -shift)


def get_user_choice():
    print("\n🔐 Secret Code Generator 🔐")
    print("1. Encode a message")
    print("2. Decode a message")
    print("3. Exit")
    choice = input("Enter your choice (1/2/3): ")
    return choice


def main():
    while True:
        choice = get_user_choice()

        if choice == "1":
            message = input("Enter the message to encode: ")
            try:
                shift = int(input("Enter shift number: "))
                encoded = encode_message(message, shift)
                print("🔒 Encoded Message:", encoded)
            except ValueError:
                print("⚠️ Please enter a valid number for shift.")

        elif choice == "2":
            message = input("Enter the message to decode: ")
            try:
                shift = int(input("Enter shift number used during encoding: "))
                decoded = decode_message(message, shift)
                print("🔓 Decoded Message:", decoded)
            except ValueError:
                print("⚠️ Please enter a valid number for shift.")

        elif choice == "3":
            print("Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please select 1, 2, or 3.")

# Run the program
main()
