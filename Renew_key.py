#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Script para usar con SecureCRT.
# GITHUB: https://github.com/kentron2019/SecureCRT_Integration_Keepass.git
# Version = 1.0
# Author = Karim Zin El Abidine El Alaoui.
# correo: kentron.dna@gmail.com

import sys
import os
import keepasshttp
from keepasshttp import KeePassHTTP
from pathlib import Path

Fichero = Path("./keepasshttp_key")

if Fichero.is_file():
    # file exists
    print("Fichero keepasshttp_key existe")
    os.remove("./keepasshttp_key")
    print("Fichero:keepasshttp_key, borrado para renovar la llave")
else:
    print("Fichero keepasshttp_key no existe, se genera una nueva llave")

    

kph = KeePassHTTP(
    #Genera la llave en la primera conexión hay que validar desde KeePass Password Safe
    storage="./keepasshttp_key", 
    url="http://localhost:19455")
hey = kph.get( "192.168.1.1" )