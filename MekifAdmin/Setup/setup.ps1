function Install-Python {
    if (-not(Test-Path -Path $python_outpath -PathType Leaf)) {
    try {
        Write-Host "Downloading Python $python_version..."
        $wc = New-Object System.Net.WebClient
        $wc.DownloadFile($python_url, $python_outpath)
    
    }
    catch {
        throw $_.Exception.Message
    }


    Write-Host "Installing python $python_version..."
    .\python-3.10.8.exe /wait /quiet InstallAllUsers=0 PrependPath=1 Include_test=0

    }
}

function Download-Files {
    # client.exe
    if (-not(Test-Path -Path $clientEXE_outpath -PathType Leaf)) {
        try {
            Write-Host "Downloading client.exe..."
            $wc = New-Object System.Net.WebClient
            $wc.DownloadFile($clientEXE_url, $clientEXE_outpath)
    
        }
        catch {
            throw $_.Exception.Message
        }
    }

    # client.png
    if (-not(Test-Path -Path $clientPNG_outpath -PathType Leaf)) {
        try {
            Write-Host "Downloading client.png..."
            $wc = New-Object System.Net.WebClient
            $wc.DownloadFile($clientPNG_url, $clientPNG_outpath)
    
        }
        catch {
            throw $_.Exception.Message
        }
    }

    # client.bat
    if (-not(Test-Path -Path $clientBAT_outpath -PathType Leaf)) {
        try {
            Write-Host "Downloading client.bat..."
            $wc = New-Object System.Net.WebClient
            $wc.DownloadFile($clientBAT_url, $clientBAT_outpath)
    
        }
        catch {
            throw $_.Exception.Message
        }
    }

    # client.vbs
    if (-not(Test-Path -Path $clientVBS_outpath -PathType Leaf)) {
        try {
            Write-Host "Downloading client.vbs..."
            $wc = New-Object System.Net.WebClient
            $wc.DownloadFile($clientVBS_url, $clientVBS_outpath)
    
        }
        catch {
            throw $_.Exception.Message
        }
    }

    # updater.exe
    if (-not(Test-Path -Path $updaterEXE_outpath -PathType Leaf)) {
        try {
            Write-Host "Downloading updater.exe..."
            $wc = New-Object System.Net.WebClient
            $wc.DownloadFile($updaterEXE_url, $updaterEXE_outpath)
    
        }
        catch {
            throw $_.Exception.Message
        }
    }

    # requirements.txt
    if (-not(Test-Path -Path $requirements_outpath -PathType Leaf)) {
        try {
            Write-Host "Downloading requirements.txt..."
            $wc = New-Object System.Net.WebClient
            $wc.DownloadFile($requirements_url, $requirements_outpath)
    
        }
        catch {
            throw $_.Exception.Message
        }
    }

}

# Destination path
$dst_path = 'C:\Peach'

# Windows startup folder for all users
$startup_path = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp"

# Python Vars
$python_version = "3.10.8"
$python_url = "https://www.python.org/ftp/python/3.10.8/python-3.10.8-amd64.exe"
$python_outpath = "$PSScriptRoot/python-3.10.8.exe"

# Github files links
$clientEXE_url = "https://github.com/GShwartz/Python/raw/main/MekifAdmin/Setup/client.exe"
$clientEXE_outpath = "$dst_path\client.exe"

$clientPNG_url = "https://github.com/GShwartz/Python/raw/main/MekifAdmin/Setup/client.png"
$clientPNG_outpath = "$dst_path\client.png"

$clientBAT_url = "https://raw.githubusercontent.com/GShwartz/Python/main/MekifAdmin/Setup/client.bat"
$clientBAT_outpath = "$dst_path\client.bat"

$clientVBS_url = "https://raw.githubusercontent.com/GShwartz/Python/main/MekifAdmin/Setup/client.vbs"
$clientVBS_outpath = "$dst_path\client.vbs"

$updaterEXE_url = "https://github.com/GShwartz/Python/raw/main/MekifAdmin/Setup/updater.exe"
$updaterEXE_outpath = "$dst_path\updater.exe"

$requirements_url = "https://raw.githubusercontent.com/GShwartz/Python/main/MekifAdmin/Setup/requirements.txt"
$requirements_outpath = "$dst_path\requirements.txt"

# Start installation
Write-Host "Installing Peach Client..."

# Install python
Install-Python

# Create local folder
Write-Host "Creating Dir Peach..."
New-Item -ItemType Directory -Force -Path "C:\Peach"

# Download client files
Download-Files

# Install python requirements
pip install -r c:\Peach\requirements.txt

# Create Defender Exclusion for EXE File
Write-Host "Creating an Exclusion for Windows Defender..."
Add-MpPreference -ExclusionPath "$PSScriptRoot"
Add-MpPreference -ExclusionPath "$dst_path"
Add-MpPreference -ExclusionPath "$startup_path"

# Print Out Defender's Exclusion List
Get-MpPreference | Select-Object -Property ExclusionPath
Write-Host "Done!"

# Set Autorun in Registry
Write-Host "Setting up persistence..."
$persistence = Set-Itemproperty -Path 'HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\Run' -Name 'Peach' -Value 'c:\Peach\client.bat' -Force
Write-Host "Done."

# Open Port 55400 For Incoming & Outgoing Traffic
Write-Host "Opening Port 55400..."
New-NetFirewallRule -DisplayName "Allow Incoming Port 55400 For Peach" -Direction Inbound -Profile Any -Action Allow -LocalPort 55400 -Protocol TCP
New-NetFirewallRule -DisplayName "Allow Outgoing Port 55400 For Peach" -Direction Outbound -Profile Any -Action Allow -LocalPort 55400 -Protocol TCP
Write-Host "Done!"

Write-Host "Installation completed, cleaning up..."
Remove-Item $python_outpath

# Run client
Write-Host "Running client..."
wscript "c:\Peach\client.vbs"