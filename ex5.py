from argparse import ArgumentError

def validate_dict(rules, dictionary):
    
    if type(dictionary) != dict and type(rules) != set:
        raise ArgumentError("Please input a dict type variable as dictionary.")

        
    returnValue = True

    for key in dictionary:
        selectedRule = False

        for rule in rules:
            if key == rule[0]:
                selectedRule = rule
                break

        if selectedRule == False:
            continue
        
        value = str(dictionary[key])
        if value.index(selectedRule[1]) != 0:
            returnValue = False
            break
        elif value[::-1].index(selectedRule[3][::-1]) != 0:
            returnValue = False
            break
        elif value[len(selectedRule[1]):len(value) - len(selectedRule[3])].index(selectedRule[2]) == -1:
            returnValue = False
            break

    return returnValue
                
inputSet = set({("aaa", "aaa", "bbb", "ccc"), ("bbb", "111", "222", "333"), ("ccc", "ggg", "hhh", "iii")})
inputDict = dict(aaa="aaacbbbcccc",bbb="111c222ccc333",ccc="gggccchhhgggiii")
print(validate_dict(inputSet, inputDict))
        