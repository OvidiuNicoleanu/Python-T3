from argparse import ArgumentError

def countElements(inputList):
    if type(inputList) != list:
       print("Please input valid arguments!")
       return
    
    a = 0
    b = 0
    alreadyCounted = list()

    for element in inputList:
        if inputList.count(element) == 1:
            a += 1
        elif element not in alreadyCounted:
            alreadyCounted.append(element)
            b += 1
    
    return (a, b)

print(countElements([1, 1, 2, 3, 4, 4, 5]))