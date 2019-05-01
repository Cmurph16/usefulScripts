#!/usr/bin/python
from Crypto import Random
from Crypto.Cipher import AES
from argparse import ArgumentParser

def make16Bytes(text):
    size = len(text)
    if (size%16 != 0):
        text += ' '*(16-(size%16))
    return text

def encrypt(text):
    # DO NOT USE THIS AS THE KEY. IT IS TEMPORARY IN ORDER TO PROVIDE ONE THAT WORKS
    # KEY NEEDS TO BE 16 BYTES
    key = 'zzzzzzzzzzzzzzzz'
    cip= AES.new(key, AES.MODE_ECB, iv)
    msg = cip.encrypt(iv+make16Bytes(text))
    return msg

def decrypt(text):
    key = 'zzzzzzzzzzzzzzzz'
    iv=text[:16]
    cip= AES.new(key, AES.MODE_ECB, iv)
    msg = cip.decrypt(text[16:])
    return msg


if __name__ == '__main__':
    parser=ArgumentParser()
    parser.add_argument('-e', '--encrypt', help='encrypt files', action='store_true', dest='encrypt')
    parser.add_argument('-d', '--decrypt', help='decrypt files', action='store_true', dest='decrypt')
    args=parser.parse_args()
    if not (args.encrypt or args.decrypt):
        parser.error('No action requested. Either -e or -d is necessary')
    iv = Random.new().read(AES.block_size)
    print(encrypt('aaa'))
    print(decrypt(encrypt('aaa')))