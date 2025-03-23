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
    shiftAmount = input( "Please enter a key (whole number from 1-25): ")
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