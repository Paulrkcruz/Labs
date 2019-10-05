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




# Write a program to draw a rectangle on the command line.
# Prompt the user for a desired width in columns (assume good input).
# Prompt the user for a desired height in rows (assume good input).
# Prompt the user for a character that you will use to draw the rectangle. The character
# can be any single letter, number, or punctuation mark except space (assume good
# input).
