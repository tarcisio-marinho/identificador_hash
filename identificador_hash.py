#!/usr/bin/env python
# identificador de hashs
# By Tarcisio Marinho
# github.com/tarcisio-marinho

def identifier(hash):
    if(hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True):
        tam=len(hash)
        if(tam==32):
            print "[+] md5"
        elif(tam==56):
            print "[+] SHA 224"
        elif(tam==64):
            print "[+] SHA 256"
        elif(tam==96):
            print "[+] SHA 384"
        elif(tam==128):
            print "[+] SHA 512"
        elif (tam==40):
            print "[+] SHA1"
        elif (tam==16):
            print "[+] base64"
        else:
            print " Hash nao encontrado"
    else:
        print "Formato incorreto"
    print "\n"
logo = '''
 .___________________.
 |  ________________ |
 | |               | |
 | | IDENTIFICADOR | |
 | |     de        | |
 | |    HASH       | |
 | |_______________| |
 !___________________!
     ._[_______]_.
 .___|___________|___.
'''
print('BEM VINDO AO IDENTIFICADOR DE HASH!\n')
linha=' ===================================='
print(logo)
while True:
    print(linha)
    hash = raw_input("HASH: ")
    print('\n')
    identifier(hash)
