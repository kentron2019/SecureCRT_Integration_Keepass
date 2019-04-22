# SecureCRT Integration Keepass

Connect to keepass from SecureCRT to obtain the user and password.
The goal is to have all the users and passwords stored in KeePass.

This development in an initial version to be able to use it from SecureCRT with the plugin
already developed by Perry Nguyen that allows retrive login and password with Chrome and Firefox browser.


Read this in other languages: <a href="https://github.com/kentron2019/SecureCRT_Integration_Keepass/blob/master/README.es.md">Spanish</a>


How does it work?
----------------

In each of the saved session of SecureCRT we load the provided .vbs file and in the argument field we put the IP that we want to connect.
This field of Argument with the IP is used to consult KeePass and obtain the username and password.
Previously in Keepass APP you have to save the user, the password and in the URL field: (In this case will be our IP).

The .vbs script will be responsible interact with Securecrt active remote sehell and for executing the python script Generic_Conector.py that is used to retrive login and password from Keepass APP.

In the SecureCRT you will have to validate all the credentials by referencing them or saving them by your IP in the URL field.


How to start?
--------------
We create a folder for example in:
Mkdir C: \ Users \ [user_windows] \ AppData \ Roaming \ VanDyke \ k-script \ 

Inside the folder Clone the proyect with git for windows:

git clone https://github.com/kentron2019/SecureCRT_Integration_Keepass.git


In each Securecrt session property load this file: SecureCRT_Keepass.vbs
To load this file in session stored go to: Properties->Connection->Logon Actions.

* It will be necessary to edit and modify the path where the Generic_Conector.py file is mencioned:

strcommand = "cmd /c python C:\Users\karim.zin\AppData\Roaming\VanDyke\k-script\SecureCRT_Integration_Keepass\Generic_Conector.py" & Chr(32) & Trim(args) &  " LoginyPassword"

Replace: "karim.zin" by you own user.

<b>Important</b>:
* This modification must be done in the file: SecureCRT_Keepass.vbs otherwise it will not work.


Pre requirements
----------------

The Generic_Conector.py file needs to have the library installed:

https://github.com/pfn/keepasshttp.git

pip install keepasshttp

* Important to follow the installation manual explained by Perry Nguyen.

One each session of SecureCRT within "connection" -> "Logon Actions" One properties this option have to be activated:

- Display logo prompts in terminal windows

It is important that this is activated.


Versions
--------

This development has been tested in the environment:

- SecureCRT (Versión: 8.5.3)
- Chrome (Versión: 73.0.3683.103 (Build oficial) (64 bits))
- Python (Versión: Python 2.7.12)
- Tested also with Python (Versión: Python 3.6.4)
- KeePass Password Safe (Versión: 2.40)
- KeePAss Plugin: KeePassHttp (Versión: 1.8.4.2)


Author:
------

Karim Zin El Abidine El Alaoui
- Creation date: 4/14/2019
- Date modified: 4/19/2019

Development version
-------------------
- Version: 1.1 - Development code to make queries using the KeepassHttp plugin.
- Version: 1.2 - A single query is made to SecureCRT instead of two to obtain the login and password.
- Version: 1.3 - The routine conexion_session (File vbs) has been improved to detect the prompt correctty in SecureCRT.