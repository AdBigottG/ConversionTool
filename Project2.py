import sys 
# Adrian Bigott
# COP2002-OT1
# December 7, 2025
# Project Part  1
# Gaining technical skills using Python in a larger program than the exercises. 

# Function created for convert from Hexadecimal to Binary
def hexToBin(hexValue):

    # Clean the string 
    hexValue = hexValue.replace("0x", "")
    hexValue = hexValue.upper()  
    
    # Create a lookup dictionary for hex to decimal
    hexToDecDict = {
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
        '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11,
        'C': 12, 'D': 13, 'E': 14, 'F': 15}
    
    # Convert hexadecimal to decimal
    decValue = 0
    power = 0
    for i in range(len(hexValue) - 1, -1, -1):
        digit = hexToDecDict[hexValue[i]]
        decValue += digit * (16 ** power)
        power += 1
    if decValue == 0:
        return "0"
    
    # Decimal to Binary 
    binValue = ""
    while decValue > 0:
        binValue = str(decValue % 2) + binValue
        decValue //= 2
    return binValue

# Function created for convert from Binary to Hexadecimal
def binToHex(binValue):

    # Clean the string
    binValue = binValue.replace("0b", "")
    
    # Convert binary to decimal
    decValue = 0
    power = 0
    for i in range(len(binValue) - 1, -1, -1):
        digit = int(binValue[i]) 
        decValue += digit * (2 ** power)
        power += 1
    if decValue == 0:
        return "0"
    
    # Create a lookup list for decimal to hex
    hexDigits = "0123456789ABCDEF"
    
    # Decimal to Hexadecimal
    hexValue = ""
    while decValue > 0:
        hexValue = hexDigits[decValue % 16] + hexValue
        decValue //= 16
    return hexValue

# Function created for convert from Decimal to Binary    
def decToBin(decValue):

    # Change the value to a interger in case that came as string 
    decValue = int(decValue)
    if decValue == 0:
        return "0"
    # Empty string for create the binary number 
    binValue = ""
    while decValue > 0:
        # Math calculation for get the binary number 
        binValue = str(decValue %2) + binValue
        decValue //= 2
    return binValue

# Function created for convert from Binary to Decimal
def binToDec(binValue):

    # Clean the string  
    binValue = binValue.replace("0b", "")
    
    # Convert from Binary to Decimal
    decValue = 0
    
    # Iterate through binary string from left to right
    for digit in binValue:
        decValue = decValue * 2 + int(digit)
    
    return decValue

def menu():
    # start of the loop
    while 5 > 0:

        # Prompt fot the menu
        print("Number Conversion Menu")
        print("1. Hexadecimal to Binary")
        print("2. Binary to Hexadecimal")
        print("3. Decimal to Binary")
        print("4. Binary to Decimal")
        print("5. Exit")
        print("")

        # prompt for the user choose an option
        userInput = input("Choose an option (1-5): ")
        
        # error message 
        while userInput not in ['1','2','3','4','5']:
            userInput = input("Invalid choice. choose an option (1-5): ")
        print("")

        # convert hex to binary
        if userInput == "1":
            hexInput=input("Enter a hexadecimal value: ")
            resultB = hexToBin(hexInput)
            nibbleSpace = ""
            for i in range(0, len(resultB), 4):
                if i > 0:
                    nibbleSpace += ' '
                nibbleSpace += resultB[i:i+4]
            print(f"Binary: {nibbleSpace}")
            print("")

        # convert binary to hex
        elif userInput == "2":
            binInput = input("Enter a binary value: ")
            resultH = binToHex(binInput)
            print(f"Hexadecimal: {resultH}")
            print("")

        # convert decimal to binary
        elif userInput == "3":
            decInput = input("Enter a decimal value: ")
            resultD = decToBin(decInput)
            print(f"Binary: {resultD}")
            print("")

        # convert binary to decimal
        elif userInput == "4":
            binInput2 = input("Enter a binary value: ")
            resultB2 = binToDec(binInput2)
            print(f"Decimal: {resultB2}")
            print("")

        # exit the program
        else:
            userInput == "5"
            print("Exiting Program")
            sys.exit(0)    
    menu()

def main():
    menu()

if __name__ == "__main__":
    main()