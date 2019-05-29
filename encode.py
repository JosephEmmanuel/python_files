# This is my program which can do simple encode & decode.
# The program codes letters in a unique way.
#
# Author:Joseph Emmanuel
# Date:18-Apr-2019
#

# from string import maketrans # Required to call maketrans function.

def encode(mesg):
    """ this function encode the message string and returns the encoded string """
    intable = 'abcdefghijklmnopqrstuvwxyz'
    outtable ='bcdefghijklmnopqrstuvwxyza'
    translationtable=str.maketrans(intable, outtable)
    encoded=mesg.translate(translationtable)    
    return (encoded)


def decode(mesg):
    """ this function decode the message string and returns the decoded string """
    intable = 'bcdefghijklmnopqrstuvwxyza'
    outtable ='abcdefghijklmnopqrstuvwxyz'
    translationtable=str.maketrans(intable, outtable)
    print("Translation table:",translationtable)
    decoded=mesg.translate(translationtable)    
    return (decoded)
    


mesg=input("Enter text to encode:")
secretmesg=encode(mesg)
print("Encoded message :",secretmesg)

decodedmesg=decode(secretmesg)
print("Decoded message :",decodedmesg)

