# This is my second program which can do simple decoding.
# The program decodes letters in a unique way.
#
# Author : Joseph Emmanuel
# Date : 18-Apr-2019


# from string import maketrans # Required to call maketrans function.

def decode(mesg):
    """ this function encode the message string and returns the encoded string """
    intable = 'bcdefghijklmnopqrstuvwxyza'
    outtable ='abcdefghijklmnopqrstuvwxyz'
    translationtable=str.maketrans(intable, outtable)
    decoded=mesg.translate(translationtable)    
    return (decoded)
    


mesg=input("Enter text to decode:")
#mesg="uif dpotfrvfodf."  #used this line for testing
 
secretmesg=decode(mesg)
print(secretmesg)





















