#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Script para usar con SecureCRT.
# GITHUB: https://github.com/kentron2019/SecureCRT_Integration_Keepass.git
# Version = 1.0
# Author = Karim Zin El Abidine El Alaoui.
# correo: kentron.dna@gmail.com

import sys
import keepasshttp
from keepasshttp import KeePassHTTP

def get_pass(recibir_todo):

    kph = KeePassHTTP(
        #Genera la llave en la primera conexión hay que validar desde KeePass Password Safe
        storage="./keepasshttp_key", 
        url="http://localhost:19455")
    hey = kph.get( str(recibir_todo[0]) )

    if str(recibir_todo[1]) =='login':
        print(hey.login)
    elif str(recibir_todo[1]) =='password':
        print(hey.password)
    else:
        print("error")

if __name__ == "__main__":
	recibir_todo = sys.argv[1], sys.argv[2]
    # [1] IP
    # [2] Login o password.
	get_pass(recibir_todo)