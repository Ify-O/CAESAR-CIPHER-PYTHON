#Define a function called getDoubleAlphabet that takes a string argument and concatenates, or combines, the given string with itself.
def getDoubleAlphabet(alphabet):
    doubleAlphabet = alphabet + alphabet
    return doubleAlphabet
# Example usage
sample_input = "ABC"
result = getDoubleAlphabet(sample_input)
print(result)

def getMessage():
    stringToEncrypt = input("Please enter a message to encrypt: ")
    return stringToEncrypt
# The cipher key is how far you will shift the letters. By using two alphabets, you can have a cipher key that is any integer from 1 to 25. Don’t count the key at index 26 because that key would shift you back to the original message.
# Define a function to request a cipher key from the user
def getCipherKey():
    shiftAmount = input( "Please enter a key (whole number from 1-50): ")
    return shiftAmount
#Encrypting a message
#Planning out the algorithm
#Take three arguments: the message, the cipherKey, and the alphabet.
# Initialize variables.
#Use a for loop to traverse each letter in the message.
#For a specific letter, find the position.
#For a specific letter, determine the new position given the cipher key.
# If current letter is in the alphabet, append the new letter to the encrypted message.
#If current letter is not in the alphabet, append the current letter.
# Return the encrypted message after exhausting all the letters in the message.

def encryptMessage(message, cipherKey, alphabet):
    encryptedMessage = ""
    uppercaseMessage = ""
    uppercaseMessage = message.upper()
    for currentCharacter in uppercaseMessage:
        position = alphabet.find(currentCharacter)
        newPosition = position + int(cipherKey)
    if currentCharacter in alphabet:
        encryptedMessage = encryptedMessage + alphabet[newPosition]
    else:
        encryptedMessage = encryptedMessage + currentCharacter
    return encryptedMessage
# Decrypting a message
#Reuse the `encryptMessage()` function for `decryptMessage()` by passing a negative cipher key to shift each letter back and reverse the encryption.
def decryptMessage(message, cipherKey, alphabet):
    decryptKey = -1 * int(cipherKey)
    return encryptMessage(message, decryptKey, alphabet)
# Creating a main function
# Logic
# Define a string variable to contain the English alphabet.
# To be able to shift letters, double your alphabet string.
#  Get a message to encrypt from the user.
# Get a cipher key from the user.
# Encrypt the message.
# Decrypt the message.
def runCaesarCipherProgram():
    myAlphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(f'Alphabet: {myAlphabet}')
    myAlphabet2 = getDoubleAlphabet(myAlphabet)
    print(f'Alphabet2: {myAlphabet2}')
    myMessage = getMessage()
    print(myMessage)
    myCipherKey = getCipherKey()
    print(myCipherKey)
    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet2)
    print(f'Encrypted Message: {myEncryptedMessage}')
    myDecryptedMessage = decryptMessage(myEncryptedMessage, myCipherKey, myAlphabet2)
    print(f'Decypted Message: {myDecryptedMessage}')
runCaesarCipherProgram()