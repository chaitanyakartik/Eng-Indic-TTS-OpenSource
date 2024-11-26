# -*- coding: utf-8 -*-

import os
import sys
import subprocess

# Ensure UTF-8 encoding
os.environ['PYTHONIOENCODING'] = 'utf-8'
sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

from translator_model import translator_model

en2indic_model = translator_model(enindic_path="E:\Projects\Multilingual_TTS\en-indic",
                                         fairseq_path="E:\Projects\Multilingual_TTS\fairseq",
                                         indicTrans_path="E:\Projects\Multilingual_TTS\indicTrans")

ta_sents = ['One dead as Bangladeshi Hindus protest denial of bail to ISKCON leader Chinmoy Krishna Das Brahmachari']

translated = en2indic_model.batch_translate(ta_sents, 'en', 'hi')
translated_str = ' '.join(translated)

#translated = 'नासिक जिले के नंदगांव निर्वाचन क्षेत्र में एकनाथ शिंदे के नेतृत्व वाले शिवसेना उम्मीदवार सुहास कांडे और राकांपा (अजित पवार) के शीर्ष नेता छगन भुजबल के भतीजे निर्दलीय उम्मीदवार समीर भुजबल के बीच एक मतदान केंद्र पर हाथापाई हो गई'
print(translated_str)


ps1_file_path = r"E:\Projects\Multilingual_TTS\run_tts.ps1"

# Command to run the PowerShell script with arguments
# Modify the command to pass arguments directly
command = [
    "powershell",
    "-ExecutionPolicy", "Bypass",
    "-File", ps1_file_path,
    translated_str,  # First argument
    "male",      # Second argument
    "hindi",     # Third argument
    "output4.wav"  # Fourth argument
]
# Run the PowerShell script
try:
    result = subprocess.run(command, check=True, capture_output=True, text=True, encoding='utf-8')
    print("PowerShell script executed successfully.")
    print(result.stdout)  # Print the output of the script
    print(result.stderr)
except subprocess.CalledProcessError as e:
    print(f"Error executing PowerShell script: {e}")
