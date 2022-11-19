Dim WShell
Set WShell = CreateObject("WScript.Shell")
WShell.Run "c:\handsoff\client.exe", 0
Set WShell = Nothing