# Global variables
possibleCharacters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
shiftedMessage = ""

# Function to perform encryption or decryption
def caesar_cipher(message, key, mode):
    shiftedMessage = ""
    for character in message.upper():  # Ensure all characters are uppercase
        if character in possibleCharacters:
            initialPosition = possibleCharacters.find(character)
            if mode == "encrypt":
                shiftedPosition = (initialPosition + key) % len(possibleCharacters)
            elif mode == "decrypt":
                shiftedPosition = (initialPosition - key) % len(possibleCharacters)
            shiftedMessage += possibleCharacters[shiftedPosition]
        else:
            shiftedMessage += character  # Leave non-alphabet characters unchanged
    return shiftedMessage

# Main code
def main():
    print("Welcome! This program will encrypt or decrypt your secret message using the Caesar cipher.\n")
    initialMessage = input("What is your message? ")

    # Key input validation
    while True:
        try:
            key = int(input("What is the key? Choose a number from 0 to 25. "))
            if 0 <= key <= 25:
                break
            else:
                print("Please enter a valid key (0-25).")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Mode input validation
    while True:
        mode = input("Do you want to encrypt or decrypt? ").lower()
        if mode in ["encrypt", "decrypt"]:
            break
        else:
            print("Invalid choice. Please type 'encrypt' or 'decrypt'.")

    # Call the function and print the result
    result = caesar_cipher(initialMessage, key, mode)
    print(f"Your {mode}ed message is: {result}")

if __name__ == "__main__":
    main()
