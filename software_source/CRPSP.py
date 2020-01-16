#!/bin/python3
import sys
import os
from ui import *
import encrypt
import decrypt

def  main(protocol='encrypt or decrypt'):
    if protocol == 'encrypt':
        encrypt.main()
    elif protocol == 'decrypt':
        decrypt.main()
    else:
        title('E R R O R')
        print("There's been a bug... Sorry about that.")

if __name__ == "__main__":
    title('C R P S P')
    print('Cesium Radioactivity Perfect Secrecy Protocol')
    space(2)
    user_protocol_choice = multiple_choices('Why are you consulting this service?', ['to encrypt a message.', 'to decrypt a message.'], 'We registered that you consulted this service ')
    if user_protocol_choice == 'to decrypt a message.':
        main("decrypt")
    elif user_protocol_choice == 'to encrypt a message.':
        main('encrypt')
    else:
        main("There's been a bug... Sorry about that.")
