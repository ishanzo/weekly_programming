# 1. "qwertyuiop"
# 2. "asdfghjkl"
# 3. "zxcvbnm,."
# The first digit of the key (e.g. 1) is the movement for the first line.
# The second digit of the key (e.g. 2) is the movement for the second line.
# The third digit of the key (e.g. 7) is the movement for the third line.
#lowecase and uppercase keys
keyboard = (
            ("qwertyuiop",0), ("QWERTYUIOP",0), ("asdfghjkl",1),
            ("ASDFGHJKL",1), ("zxcvbnm,.",2), ("ZXCVBNM<>",2)
)
#joining all the keys together in one string
total_keys = "".join(keys[0] for keys in keyboard)
#function for encrypting
def encrypt(text, num):
    if num == 0: #if the num is 0 (no moves)
        return text
    num = str(num).zfill(3) #making it into a string
 #no zeros will be added if num has three digits
    encrypt_msg = '' #var for encrypted message
    for x in text:#iterate over text input
        if x not in total_keys:
            encrypt_msg += x
        for keys,row in keyboard: #iterate over 2d array of keys
            if x in keys:
                shift = num[row] #shift is the input num row
                encrypt_letter = keys[(keys.index(x) + int(shift))%len(keys)]#encrypted letter
                encrypt_msg += encrypt_letter #for every letter
    return encrypt_msg #output
# _____________________________________________________________________
def decrypt(text, num):
    if num == 0:##if the num is 0 (no moves)
        return text
    num = str(num).zfill(3) #making it into a string
     #no zeros will be added if num has three digits
    decrypt_msg = ''#var for encrypted message
    for x in text:#iterate over text input
        if x not in total_keys:
            decrypt_msg += x
        for keys, row in keyboard:##iterate over 2d array of keys
            if x in keys:
                shift = num[row]
                decrypt_letter = keys[(keys.index(x) - int(shift) + len(keys))%len(keys)]# minus
                decrypt_msg += decrypt_letter
    return decrypt_msg
