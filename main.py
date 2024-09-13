import string

# Global variables
lettersLower = string.ascii_lowercase
lettersUpper = string.ascii_uppercase
numbers = string.digits
symbols = string.punctuation
possibleCharacters = lettersLower + lettersUpper + numbers + symbols

# Define the function called encryptOrDecrypt
def encryptOrDecrypt(initialPosition, key, mode):
    """
    Encrypts or decrypts a character based on the given mode and key.
    """
    if mode.lower() == "encrypt":
        return (initialPosition + key) % len(possibleCharacters)
    elif mode.lower() == "decrypt":
        return (initialPosition - key) % len(possibleCharacters)

# Define the function called wraparound
def wraparound(shiftedPosition):
    """
    Adjusts the shifted position to wrap around if necessary.
    """
    return shiftedPosition % len(possibleCharacters)

# Run code

# Introduction
print("Welcome! This program will encrypt or decrypt your secret message using the Caesar cipher.")
print(f"Allowed characters: {possibleCharacters}\n")

# Receive user input
initialMessage = input("What is your message? ")
try:
    key = int(input("What is the key? Choose a number from 0 to 93. "))
    if not (0 <= key <= 93):
        raise ValueError("Key out of range.")
except ValueError as e:
    print(f"Invalid input: {e}")
    exit(1)

mode = input("Do you want to encrypt or decrypt? ").lower()
if mode not in ["encrypt", "decrypt"]:
    print("Invalid mode. Please type 'encrypt' or 'decrypt'.")
    exit(1)

# Encrypt or decrypt the message
shiftedMessage = ""
for character in initialMessage:
    if character in possibleCharacters:
        initialPosition = possibleCharacters.find(character)
        shiftedPosition = encryptOrDecrypt(initialPosition, key, mode)
        shiftedPosition = wraparound(shiftedPosition)
        shiftedMessage += possibleCharacters[shiftedPosition]
    else:
        shiftedMessage += character

# Print the shifted message
print(f"Your {mode}ed message is: {shiftedMessage}")
