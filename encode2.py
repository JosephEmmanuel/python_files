# This is my second decoding program using functions
# not yet complete
# Made by : Joesph Em T
# Date : 28\5\2018

def encode(mesg):
    intable = 'abcdefghijklmnopqrstuvwxyz'
    outtable ='1a2b3c4d5e6f7g8h9i0jklmnop'
    translationtable=str.maketrans(intable, outtable)
    encoded=mesg.translate(translationtable)    
    return (encoded)


def decode(mesg):
    intable = '1a2b3c4d5e6f7g8h9i0jklmnop'
    outtable ='abcdefghijklmnopqrstuvwxyz'
    translationtable=str.maketrans(intable, outtable)
    print("Translation table:",translationtable)
    decoded=mesg.translate(translationtable)    
    return (decoded)
