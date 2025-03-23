#Define a function called getDoubleAlphabet that takes a string argument and concatenates, or combines, the given string with itself.
def getDoubleAlphabet(alphabet):
    doubleAlphabet = alphabet + alphabet
    return doubleAlphabet
# Example usage
sample_input = "ABC"
result = getDoubleAlphabet(sample_input)
print(result)