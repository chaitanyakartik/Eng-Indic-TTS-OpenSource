# Setup Script for TTS Project Without Conda

# Step 1: Install Git LFS
Write-Host "Installing Git LFS..."
Invoke-WebRequest -Uri "https://packagecloud.io/install/repositories/github/git-lfs/script.ps1" -OutFile "install_git_lfs.ps1"
.\install_git_lfs.ps1
git lfs install

# Step 2: Clone the repository
Write-Host "Cloning repository..."
git clone https://github.com/smtiitm/Fastspeech2_HS.git
Set-Location -Path "Fastspeech2_HS"

# Step 3: Fetch all LFS files
Write-Host "Fetching Git LFS files..."
git lfs fetch --all
git lfs pull

# Step 4: Set up Python virtual environment
Write-Host "Setting up Python virtual environment..."
# python -m venv tts_env
# .\tts_env\Scripts\activate

Invoke-WebRequest https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe -o miniconda.exe
Start-Process -FilePath ".\miniconda.exe" -ArgumentList "/S" -Wait
Remove-Item miniconda.exe

# Step 1: Navigate to your project directory where the environment.yml is located
cd "E:\Projects\Multilingual_TTS\Fastspeech2_HS"

# Step 2: Create the conda environment based on environment.yml
conda env create -f environment.yml

# Step 3: Activate the conda environment
conda activate tts-hs-hifigan

# Step 4: (Optional) Install PyTorch and CUDA Toolkit
conda install pytorch cudatoolkit=11.3 -c pytorch

# Step 5: Install required Python dependencies
Write-Host "Installing Python dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Step 6: Install PyTorch and torchaudio
Write-Host "Installing PyTorch and torchaudio..."
pip install torch torchaudio --index-url https://download.pytorch.org/whl/cu118

# Step 7: Run inference
Write-Host "Running inference to synthesize speech..."
python inference.py --sample_text "Your input text here" --language hindi --gender male --alpha 1 --output_file output.wav
