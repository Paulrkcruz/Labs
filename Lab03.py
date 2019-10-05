# Paul Cruz
# 9/30/2019
# Lab 03


# Problem #1
# Write a program that asks the user to enter a positive integer, ​n,​ which is a power of 2, 
# and uses a loop​ to calculate the logarithm base 2, of ​n​. For this assignment, you can assume 
# the user gives you good input.
def log2(num):
    if num == 1:
        return 0
    else:
        count = 0
        while num > 1:
            num //= 2
            count += 1
        return count

def main():
    
    output = int(input("Enter an integer that is a positive power of 2: "))
    log2_result = log2(output )
    print("log2(" + str(output ) + ") = " + str(log2_result))

main()
    
    
# Problem #2
# We care about logarithm base 2 and powers of 2 in computer science because of the nature of circuits: 
# They understand on/off, zero/one, True/False. Values in memory (numeric, strings, machine code, 
# all of it) are stored as a collection of 0s and 1s.
# For this part of the lab:
# Prompt the user for a binary number (assume good input).
# Convert it to its decimal equivalent and print it out.
def binary_to_decimal(binary_string):
    power = 0
    totaled = 0
    for index in range(len(binary_string)-1, -1, -1):
        if binary_string[index] == "1":
            totaled += 2**power
            power += 1
        else:
            power += 1
    
    return totaled

def main():

    string_binary = input("Please enter a binary number:\n")
    converted_result = binary_to_decimal(string_binary)
    print(string_binary, "=", converted_result)

main()

# Problem 3
# Write a program to draw a rectangle on the command line.
# Prompt the user for a desired width in columns (assume good input).
# Prompt the user for a desired height in rows (assume good input).
# Prompt the user for a character that you will use to draw the rectangle. The character
# can be any single letter, number, or punctuation mark except space (assume good
# input).
def draw_rect(width, height, character):
    for row in range(height):
        for column in range(width):
            if row == 0 or row == height-1:
                print(character, end="")
            else:
                if column == 0 or column == width-1:
                    print(character, end="")
                else:
                    print(" ", end="")
        print()


def draw_rect_alt(width, height, character):
    for row in range(height):
        if row == 0 or row == height-1:
            print(character * width)
        else:
            print(character, end="")
            print(" " * (width-2), end="")
            print(character)


width = int(input("Enter a width:\n"))
height = int(input("Enter a height:\n"))
character = input("Choose a character:\n")
draw_rect(width, height, character)
draw_rect_alt(width, height, character)
