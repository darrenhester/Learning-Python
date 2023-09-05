# Example of a Python function that uses a data dictionary

hexNumbers = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4':4, '5':5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F':15 
}

# Converts a string hexidecimal number into an integer decimal
# If hexNum is not a valid hexadecimal number, returnes none

def hexToDec (hexNum):
    for char in hexNum:
        if char not in hexNumbers:
            return None
        
        if len(hexNum) == 3:
            return hexNumbers[hexNum[0]] * 256 + hexNumbers[hexNum[1]] * 16 + hexNumbers[hexNum[2]]
        
        if len(hexNum) == 2:
            return hexNumbers[hexNum[0]] * 16 + hexNumbers[hexNum[1]]
        
        if len(hexNum) == 1:
            return hexNumbers[hexNum[0]] 
        
# 10 
print (hexToDec('A'))

# 0
print (hexToDec('0'))

# 27
print (hexToDec('1B'))

# 960
print (hexToDec('3C0'))

# Invalid
print (hexToDec('ZZTop'))

