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