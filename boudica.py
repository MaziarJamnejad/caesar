#Caesar cipher codebreaker

# declare variables
plainAlphabet = "abcdefghijklmnopqrstuvwxyz"

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

# function to create multiple short plaintexts with all possible key numbers
def sampleDecryptions(ciphertext):
    print("Sample decryptions for all key numbers:")
    for keynumber in range(1, 26):
        decrypted = decryptCaesar(ciphertext, keynumber)
                
        if len(decrypted) > 20: 
            print(f"Key {keynumber}: {decrypted[:20]}...")
        else:
            print(f"Key {keynumber}: {decrypted}")
            
# inputs
ciphertext = input("Enter ciphertext: ")
sampleDecryptions(ciphertext)

choice = int(input("Which of these looks correct? Enter number (1-25): "))

if choice == 0:
    print("Invalid choice.")
elif choice < 0 or choice > 25:
    print("Invalid choice. Please choose a number between 1 and 25.")
else:
    plaintext = decryptCaesar(ciphertext, choice)
    print(f"Decrypted plaintext: {plaintext}")

