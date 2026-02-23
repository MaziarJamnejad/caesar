# declare variables
plainAlphabet = "abcdefghijklmnopqrstuvwxyz"

# function to encrypt using Caesar cipher
def encryptCaesar(plaintext, keynumber):
    ciphertext = ""
    for char in plaintext:
        if char in plainAlphabet:
            index = plainAlphabet.index(char)
            newIndex = (index + keynumber) % 26
            ciphertext += plainAlphabet[newIndex]
        elif char in plainAlphabet.upper():
            index = plainAlphabet.upper().index(char)
            newIndex = (index + keynumber) % 26
            ciphertext += plainAlphabet.upper()[newIndex]
        else:
            ciphertext += char
    return ciphertext

# function to decrypt using Caesar cipher
def decryptCaesar(ciphertext, keynumber):

    plaintext = ""
    for char in ciphertext:
        if char in plainAlphabet:
            index = plainAlphabet.index(char)
            newIndex = (index - keynumber) % 26
            plaintext += plainAlphabet[newIndex]
        elif char in plainAlphabet.upper():
            index = plainAlphabet.upper().index(char)
            newIndex = (index - keynumber) % 26
            plaintext += plainAlphabet.upper()[newIndex]
        else:
            plaintext += char
    return plaintext

# inputs
mode = input ("Do you want to encrypt or decrypt? (e/d): ").strip().lower()
if mode == "e":
    plaintext = input("Enter plaintext: ")
    keynumber = int(input("Enter shift number:"))
    ciphertext = encryptCaesar(plaintext, keynumber)
    print("Plaintext:", plaintext)
    print("Ciphertext:", ciphertext)
elif mode == "d":
    ciphertext = input("Enter ciphertext: ")
    keynumber = int(input("Enter shift number:"))
    plaintext = decryptCaesar(ciphertext, keynumber)
    print("Ciphertext:", ciphertext)
    print("Plaintext:", plaintext)
else:
    print("Invalid mode. Please choose 'e' for encrypt or 'd' for decrypt.")    