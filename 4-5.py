###
# Encrypts text using Caesar Code, shifting each letter
# in the alphabet right one position
#
plain_text = 'The early bird catches the worm'
encrypted_text = ''
shift = 1

for char in plain_text:

    # read the character's code (use ord())
    new_code = ord(char)
    # add one to the character's code
    new_code = ord(char) + shift
    if new_code > ord('z'):
            new_code = new_code - 26
    # replace new character code with its
    # corresponding character (use chr())
    encrypted_text = encrypted_text + chr(new_code)
    # add encrypted character to encrypted text

print(plain_text)
print(encrypted_text)