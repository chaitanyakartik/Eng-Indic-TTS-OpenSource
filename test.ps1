# Step 1: Install Git LFS for Windows
Write-Host "Installing Git LFS..."

# Download the Git LFS installer from the official Git LFS website
Invoke-WebRequest -Uri "https://github.com/git-lfs/git-lfs/releases/download/v3.2.0/git-lfs-windows-v3.2.0.exe" -OutFile "git-lfs-installer.exe"

# Run the installer
Start-Process -FilePath "git-lfs-installer.exe" -ArgumentList "/S" -Wait

# Initialize Git LFS
git lfs install

Write-Host "Git LFS has been installed successfully."