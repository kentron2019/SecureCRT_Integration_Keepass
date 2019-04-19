#$language = "VBScript"
#$interface = "1.0"

' Script para usar con SecureCRT.
' GITHUB: https://github.com/kentron2019/SecureCRT_Integration_Keepass.git
' Version = 1.0
' Author = Karim Zin El Abidine El Alaoui.
' correo: kentron.dna@gmail.com

Option Explicit

'Comenzamos sincronizacion con pantalla
crt.Screen.Synchronous = True

' Declaramos variables estándar.
Dim strLogin, strPassword

Const ForReading = 1
Const CiscoIosPrompt = "Username: "
Const CiscoIosPrompt2 = "username: "
Const DellChassisPrompt = "User Name:"

Sub Main 'Funcción Principal.
	
	call Consulta_keepass()

	' Credentials should be known now call userLogin
	Call conexion_session(strLogin, strPassword)

	'Terminamos sincronizacion con pantalla
	crt.Screen.Synchronous = False

End Sub


Sub Consulta_keepass()

	dim wshShell, objShell, login, password, args, strcommand_log, strcommand_pass, strcommand, list, strText, n, strPreLogin, dashCount, thisURL, strPrePassword
  	
	'Recuperamos del campo argumento la IP.
	args = crt.Arguments.GetArg(0)

	'Preparamos el comando con el scrypt python a lanzar y añadimos a la consulta la IP y tipo de consulta: login/password o amboos.
	' Path que hay que cambiar para localizar la ubicación del fichero: Generic_Conector.py
	strcommand = "cmd /c python C:\Users\karim.zin\AppData\Roaming\VanDyke\k-script\SecureCRT_Integration_Keepass\Generic_Conector.py" & Chr(32) & Trim(args) &  " LoginyPassword"

	Set objshell = createobject("wscript.shell")
	Set login = objshell.exec(strcommand)
	strText = Trim(login.stdout.readall)

	dashCount = len(strText)-len(replace(strText,"-","")) 
	n=dashCount
	thisURL=split(strText,"-")
	strPreLogin=replace(thisURL(0),".","")
	strPrePassword=replace(thisURL(1),".","")
	

	strLogin = Trim(strPreLogin)
	strPassword = Trim(strPrePassword)
	'MsgBox strLogin

End Sub


Sub conexion_session(strLogin, strPassword)
	Dim intLoginInicial

  ' Login using provided credentials, check for different prompts
  ' WaitForStrings returns index of string as result, 
  ' used to check prompt response selections or 0 = timeout
  ' 
  intLoginInicial = crt.Screen.WaitForStrings(CiscoIosPrompt, DellChassisPrompt, CiscoIosPrompt2, 3)
  If intLoginInicial > 3 Then
			MsgBox "No se puede detectar el tipo de prompt!"
			Exit Sub
		ElseIf intLoginInicial = 0 Then
			MsgBox "Timeout!, prompt no detectado :-)"
			Exit Sub
		Else
			
		    'crt.Sleep 3000
		    crt.Screen.WaitForString "login as: ", 1
			crt.Screen.Send Trim(strLogin) & chr(13)
			crt.Sleep 2000
			crt.Screen.WaitForString "assword: ", 1
			crt.Screen.Send Trim(strPassword) & chr(13)
			crt.Sleep 2000
			crt.Screen.WaitForString "username: ", 1
			crt.Screen.Send Trim(strPassword) & chr(13)
	End If
	
	' usar condición para averiguar su¡i hay acceso como enable en dispositivos cisco.
	If (crt.Screen.WaitForString("#", 1)) Or (crt.Screen.WaitForString("(enable)", 1)) Or (crt.Screen.WaitForString("*", 1))  Then
		crt.Window.Activate()
	Else
		
        'crt.Sleep 3000
		crt.Screen.WaitForString "Username: "
	    crt.Screen.Send Trim(strLogin) & chr(13)
		crt.Sleep 2000
		crt.Screen.WaitForString "assword: ", 1
		crt.Screen.Send Trim(strPassword) & chr(13)
		crt.Screen.WaitForString "#", 1		
	End If

End Sub

