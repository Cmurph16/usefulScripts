#!/usr/bin/python
# stored in /usr/local/bin as passgen
import string
import random
from argparse import ArgumentParser

letters = string.ascii_letters
numbers = '0123456789'
specialChars = '."?!@#$&*()'
allCharacters = letters+numbers+specialChars

def createPassword(length):
    passwd = ''
    for _ in range(length):
        passwd += (random.choice(allCharacters))
    return passwd

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-l', '--length', help='Given length of password. If none given then a random length between 16 and 33 is picked', dest='length', type=int)
    args = parser.parse_args()
    if(not(args.length)):
        length = random.randint(16,33)
    else:
        length = args.length
    passwd = createPassword(length)
    print(passwd)