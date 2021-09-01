#!/usr/bin/env python
"""
SYNOPSIS

    Caesar.py
    No command line arguments involved.

DESCRIPTION

    Enter a plaintext message and then the rotation key. The
    plaintext is then converted to cypher text and saved to a file.

EXAMPLES

    User enters 'Hello!' and a key of 13.
    Output should give 'Uryyb!' and write it to a file.

AUTHOR

    Joe Blog <jblogs@TMC.org>
    Gede Wirayuda <30037137@tafe.wa.edu.au>

LICENSE

    This script is in the public domain, free from copyrights or
    restrictions.

VERSION

    0.3
"""
## Scenario 2 Code ##


# Caesar cypher function
def rot(text, key):
    #set an empty string to use to append the encyrpted letter
    cypher_text = ''
    #iterates through the each character in the message
    for char in text:
        #Checks whether the character letter is in the alphabet (A-Z/a-z)
        if char.isalpha():
            #Assigns the Unicode number to the character of the letter chosen
            num = ord(char)
            #checks if the letter is an uppercase letter (Unicode # between 65 and 90)
            if num >= 65 and num <= 90:
                #checks to see if the number has gone beyond the uppercase letters range (90)
                #and if it does, it then returns back to 'A' and uses its remaining letter
                if (num + key) > 90:
                    #the remaining amount of numbers that must be be added to the unicode of 'A'
                    x = (num+key) - 90
                    #The the encrypted letter is made by adding the unicode number of 'A' and the
                    #remaining number and transforming it using chr()
                    #the encrypted letter is appended onto the encyrpted text string
                    cypher_text += cypher_text.join(chr(x + ord('A')-1))
                else:
                    #if the rotated key is not above the uppercase unicode range, it simply adds it
                    #to the cypher text string by adding the unicode number and the roated key number
                    #and transforming it with chr()
                    cypher_text += cypher_text.join(chr(num+key))
            #checks to see if the letter is a lowercase letter (Unicode number between 97 and 122)
            elif num >= 97 and num <= 122:
                #checks to see if the number has gone beyond the lowercase letters range (122)
                #and if it does, it returns it back to 'a' and uses its remaining letter
                if (num + key) > 122:
                    #the remaining amount of numbers that must be added to the Unicode of 'a'
                    x = (num + key) - 122
                    #The encrypted letter is made by adding the unicode number of 'a' and the
                    #remaining number and transforming it using chr()
                    #the encyrpted letter is appended onto the encrypted text string
                    cypher_text += cypher_text.join(chr(x + ord('a')-1))
                else:
                    #adds the encyrpted letter if the combined rotated unicode number is not above the
                    #lowercase unicode range (122) by using chr()
                    cypher_text += cypher_text.join(chr(num+key))
        else:
            #Characters that aren't letters are simply added as it is, such as numbers, symbols or spaces
            cypher_text += cypher_text.join(char)
    # Return the final result of the processed characters for use.
    return cypher_text


# Ask the user for their message
plain_input = input('Input the text you want to encode: ')
# A while loop that can only be True if the user enters a number between 0 and 25
while True:
    #asks the user to enter a rotation key between 0 and 25
    rot_key = int(input('Input the key you want to use from 0 to 25: '))
    #if the key is less than 0 and greater than 25, it prints out to enter it again
    if rot_key < 0 or rot_key > 25:
        print('Please enter  a number between 0 and 25.')
    #if the user enters a number between 0 and 25, the script is continued
    else:
        break
# Secret message is the result of the rot function
secret_message = rot(plain_input, rot_key)
# Print out message for feedback
print('Writing the following cypher text to file:', secret_message)
# Write the message to file
with open('EncyrptedFile.txt', 'w+') as file:
    file.write(secret_message)
