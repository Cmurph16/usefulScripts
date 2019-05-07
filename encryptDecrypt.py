#!/usr/bin/python
from Crypto import Random
from Crypto.Cipher import AES
from argparse import ArgumentParser, FileType
import sys

def make16Bytes(text):
    size = len(text)
    if (size%16 != 0):
        text += ' '*(16-(size%16))
    return text

def encrypt(text, key):
    cip= AES.new(key, AES.MODE_ECB, iv)
    msg = cip.encrypt(iv+make16Bytes(text))
    return msg

def decrypt(text, key):
    iv=text[:16]
    cip= AES.new(key, AES.MODE_ECB, iv)
    msg = cip.decrypt(text[16:])
    return msg

if __name__ == '__main__':
    parser=ArgumentParser()
    parser.add_argument('-e', '--encrypt', help='encrypt files', action='store_true', dest='encrypt')
    parser.add_argument('-d', '--decrypt', help='decrypt files', type=FileType('r'), default=None, dest='decrypt')
    parser.add_argument('-t', '--text', help='text to encrypt', nargs='*', dest='text',default=None)
    parser.add_argument('-f', '--file', help='inputted file to encrypt', type=FileType('r'), default=None, dest='file')
    parser.add_argument('-k', '--key', help='key for encryption and decryption', dest='key',required=True)
    args=parser.parse_args()
    if not (args.encrypt or args.decrypt != None):
        parser.error('No action requested. Either -e or -d is necessary')
    if(len(args.key)%16 != 0):
        parser.error('Key used must be divisible by 16')
    if (args.encrypt):
        if (args.file != None and args.text != None):
            parser.error('Cannot input both file and text. Select one or the other')
        if (args.file == None and args.text == None):
            parser.error("No file or text provided for encryption. Either -f or -t is required")
        if (args.file):
            inp = args.file.read()
        else:
            inp = ''.join(args.text)
        iv = Random.new().read(AES.block_size)
        outfile = open('encryptedOutput', 'w')
        outfile.write(encrypt(inp, args.key))
    else:
        outfile = open('decryptedOutput', 'w')
        outfile.write(decrypt(args.decrypt.read(), args.key))
