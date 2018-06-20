#!/usr/bin/env python
# identificador de hashs
# By Tarcisio Marinho
# github.com/tarcisio-marinho


import sys

def help():
    print("USAGE:\nidentify <hash/hashes>")
    sys.exit(-1)

def identifier(hash):
    if(hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True):
        tam=len(hash)
        if(tam==32):
            print "{} - [+] md5".format(hash)
        elif(tam==56):
            print "{} - [+] SHA 224".format(hash)
        elif(tam==64):
            print "{} - [+] SHA 256".format(hash)
        elif(tam==96):
            print "{} - [+] SHA 384".format(hash)
        elif(tam==128):
            print "{} - [+] SHA 512".format(hash)
        elif (tam==40):
            print "{} - [+] SHA1".format(hash)
        elif (tam==16):
            print "{} - [+] base64".format(hash)
        else:
            print "{} [-] Hash nao encontrado".format(hash)
    else:
        print "{} [-] Formato incorreto".format(hash)
    print "\n"

if __name__ == "__main__":
    if(len(sys.argv) < 2):
        help()

    hashes = sys.argv
    hashes.pop(0)
    for hash in hashes:
        identifier(hash)