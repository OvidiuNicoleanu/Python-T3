from argparse import ArgumentError


def listOperation(a, b):
    if type(a) != list or type(b) != list:
        raise ArgumentError("Please give valid inputs!")
    
    reunion = set(a).union(set(b))

    intersection = set(a).intersection(set(b))
    
    aMinusb = set(a).difference(set(b))
    
    bMinusa = set(b).difference(set(a))

    return [reunion, intersection, aMinusb, bMinusa]

a = [1, 2, 3, 4]
b = [2, 3, 4, 5]
print(listOperation(a, b))


