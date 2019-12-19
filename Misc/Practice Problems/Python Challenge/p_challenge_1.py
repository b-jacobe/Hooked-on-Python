"""
p_challenge_1.py
"""
# Helper Function
def shift(seq, shift=-1):
    # Added to prevent returning the same 
    # encrypted message
    if shift == 0:
        shift = 1
    return seq[-shift:] + seq[:-shift]

def word_encrypter():
    message = input("Enter the message you wish to encrypt.\n")
    val = input("Enter a random number for the encryption.\n")
    error_message = "The value you entered is incorrect."
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    if val.isnumeric() == True:
        encoded_alphabet = shift(alphabet,int(val))
        table = str.maketrans("".join(encoded_alphabet),"".join(alphabet))
        encoded_message = message.translate(table)
        return encoded_message
    else:
        return error_message




riddle = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
table = str.maketrans("abcdefghijklmnopqrstuvwxyz","cdefghijklmnopqrstuvwxyzab")
result = riddle.translate(table)
#print(result)


reverse_riddle = "This is a secret message, try and encrypt this!"

# static method that creates a one to one mapping of a character to its translation
table = str.maketrans("zyxwvutsrqponmlkjihgfedcba","abcdefghijklmnopqrstuvwxyz")
reverse_result = reverse_riddle.translate(table)
#print(reverse_result)

print(word_encrypter())