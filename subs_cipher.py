'''
'''


def encode(forward, msg):
    for letter in msg:
        if letter in forward:
            msg.split(' ')
            cipher_text = forward[letter]
    return cipher_text

def decode(forward, cipher_text):
    for letter in cipher_text:
        if letter in forward:
            decode_text = forward[letter]
    return decode_text

