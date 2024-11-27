# setup.ps1 - Setup script with careful dependency version management for PowerShell

Write-Output "Starting setup..."
# Create and activate a virtual environment (recommended)
# python -m venv venv
# .\venv\Scripts\Activate

# Upgrade pip to latest version first
python.exe -m pip install --upgrade pip

# Install specific fairseq version
pip install fairseq==0.12.2

# Downgrade pip to compatible version for other dependencies
python.exe -m pip install pip==24.0
# Install specific omegaconf version
pip install omegaconf==2.0.6
# Reinstall fairseq to resolve conflicts
pip install fairseq==0.12.2
# Install xformers
pip install xformers

# Clone required repositories
git clone https://github.com/AI4Bharat/indicTrans.git
git clone https://github.com/anoopkunchukuttan/indic_nlp_library.git
git clone https://github.com/anoopkunchukuttan/indic_nlp_resources.git
git clone https://github.com/rsennrich/subword-nmt.git
git clone https://github.com/pytorch/fairseq.git

# Install other dependencies with specific versions
pip install sacremoses pandas mock sacrebleu tensorboardX pyarrow
pip install mosestokenizer subword-nmt
pip install indic-nlp-library
pip install flask==2.0.1

# Install fairseq from source
Set-Location .\fairseq
pip install .\
Set-Location ..

# Download and extract the model
Invoke-WebRequest -Uri https://ai4b-public-nlu-nlg.objectstore.e2enetworks.net/en2indic.zip -OutFile en2indic.zip
Expand-Archive -Path en2indic.zip -DestinationPath . -Force

Write-Output "Setup complete! Activate the virtual environment with:"
Write-Output ".\venv\Scripts\Activate.ps1"
