Python Version: Python 3.9.10

Setup Instructions:
Install Miniconda first

1. First Activate virtual environment
   python -m venv venv
   .\venv\Scripts\Activate

2. Run the setup scripts for translator and tts
   .\translator_setup_script.ps1
   .\tts_setup_script.ps1

3. Make changes to some files:

   1. Change “from scipy.signal.windows import kaiser” to
      “from scipy.signal.windows import kaiser” in E:\Projects\Multilingual_TTS\venv\lib\site-packages\espnet2\gan_tts\melgan\pqmf.py

   2. Change
      “with open(f"{language}/{gender}/model/config.yaml", "r") as file: config = yaml.safe_load(file)”
      To
      “with open(f"{language}/{gender}/model/config.yaml", "r", encoding='utf-8') as file:
      config = yaml.safe_load(file)”
      In E:\Projects\Multilingual_TTS\Fastspeech2_HS\inference.py

   3. Wherever theres with open(file_path, 'w') as f:
      Change it to with open(file_path, 'w', encoding='utf-8') as f:

4. Run main.py
