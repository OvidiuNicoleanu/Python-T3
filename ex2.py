from argparse import ArgumentError

def getCharacterFrequency(inputString):
    if type(inputString) is not str:
        raise ArgumentError("Please give valid inputs!")
    
    characterFrequency = dict()
    for char in inputString:
        if char not in characterFrequency:
            characterFrequency[char] = inputString.count(char)

    return characterFrequency

inputString = input()
print(getCharacterFrequency(inputString))

    
        