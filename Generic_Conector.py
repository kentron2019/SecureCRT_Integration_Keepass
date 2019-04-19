#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Script para usar con SecureCRT.
# GITHUB: https://github.com/kentron2019/SecureCRT_Integration_Keepass.git
# Version = 1.1
# Author = Karim Zin El Abidine El Alaoui.
# correo: kentron.dna@gmail.com

import sys
import os
from pathlib import Path
import keepasshttp
from keepasshttp import KeePassHTTP

def get_pass(recibir_todo):

    Fichero = Path("./keepasshttp_key")

    kph = KeePassHTTP(
            #Genera la llave en la primera conexión hay que validar desde KeePass Password Safe
            storage="./keepasshttp_key", 
            url="http://localhost:19455")

    try:
        kph._authenticate()

    except: # Any other exception
        print(kph)
        print("type:", type(kph))
        if Fichero.is_file():
            # file exists
            print("Fichero keepasshttp_key existe")
            os.remove("./keepasshttp_key")
            print("Fichero:keepasshttp_key, borrado para renovar la llave")
            kph = KeePassHTTP(
                #Genera la llave en la primera conexión hay que validar desde KeePass Password Safe
                storage="./keepasshttp_key", 
                url="http://localhost:19455")
            hey = kph.get( str(recibir_todo[0]) )
            sys.exit(1)
    finally: # Optional
        #print("finally:")
        kph = KeePassHTTP(
            #Genera la llave en la primera conexión hay que validar desde KeePass Password Safe
            storage="./keepasshttp_key", 
            url="http://localhost:19455")
        hey = kph.get( str(recibir_todo[0]) )
        #print("Resultado de hey.login", hey.login)
        
        if str(recibir_todo[1]) =='LoginyPassword':
            resultado = str(hey.login)+str("-")+str(hey.password)
            print(resultado)
        elif str(recibir_todo[1]) =='login':
            print(hey.login)
        elif str(recibir_todo[1]) =='password':
            print(hey.password)
        else:
            print("error")

        pass # Clean up

if __name__ == "__main__":
	recibir_todo = sys.argv[1], sys.argv[2]
    # [1] IP
    # [2] Login o password.
	get_pass(recibir_todo)