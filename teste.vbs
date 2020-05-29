Dim wShell
Set wShell = CreateObject("WScript.Shell")

strComputer = "."
Set objWMIService = GetObject("winmgmts:" _
& "{impersonationLevel=impersonate}!\\" & strComputer & "\root\cimv2")

serianum = ""

Set colItems = objWMIService.ExecQuery( _
"SELECT * FROM Win32_ComputerSystemProduct")
For Each objItem in colItems
serianum = objItem.IdentifyingNumber
Next

wShell.Run "http://odoo-oca.avell.com/site_avell/"&serianum,9