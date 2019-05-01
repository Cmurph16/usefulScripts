#!/usr/bin/python
from Crypto import Random
from Crypto.Cipher import AES

iv = Random.new().read(AES.block_size)
# DO NOT USE THIS AS THE KEY. IT IS TEMPORARY IN ORDER TO PROVIDE ONE THAT WORKS
# KEY NEEDS TO BE 16 BYTES
key = 'zzzzzzzzzzzzzzzz'

cip= AES.new(key, AES.MODE_ECB, iv)
msg = cip.encrypt('Attack          ')

ret = cip.decrypt(msg)
print(msg)
print(ret)