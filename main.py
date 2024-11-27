# -*- coding: utf-8 -*-

import os
import sys
import subprocess
from translator_model import translator_model
import subprocess

# Ensure UTF-8 encoding
os.environ['PYTHONIOENCODING'] = 'utf-8'
sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

def translate_and_generate_tts(
    english_text,
    target_language,
    gender,
    output_file_path,
    enindic_path="E:\\Projects\\Multilingual_TTS\\en-indic",
    fairseq_path="E:\\Projects\\Multilingual_TTS\\fairseq",
    indicTrans_path="E:\\Projects\\Multilingual_TTS\\indicTrans",
    ps1_file_path="E:\\Projects\\Multilingual_TTS\\run_tts.ps1"
):
    # Model initialization paths
    en2indic_model = translator_model(
        enindic_path=enindic_path,
        fairseq_path=fairseq_path,
        indicTrans_path=indicTrans_path
    )
    
    # Mapping dictionaries
    languages_tl_model_keywords = {
        "Assamese": "as",
        "Bengali": "bn",
        "Gujarati": "gu",
        "Hindi": "hi",
        "Kannada": "kn",
        "Malayalam": "ml",
        "Marathi": "mr",
        "Odia": "or",
        "Punjabi": "pa",
        "Tamil": "ta",
        "Telugu": "te"
    }
    
    languages_tts_model_keywords = {
        "Assamese": "assamese",
        "Bengali": "bengali",
        "Gujarati": "gujarati",
        "Hindi": "hindi",
        "Kannada": "kannada",
        "Malayalam": "malayalam",
        "Marathi": "marathi",
        "Odia": "odia",
        "Punjabi": "punjabi",
        "Tamil": "tamil",
        "Telugu": "telugu"
    }
    
    # Check if the target language is supported
    if target_language not in languages_tl_model_keywords:
        raise ValueError(f"Target language '{target_language}' is not supported.")
    
    # Get the translation language code and TTS model keyword
    target_lang_code = languages_tl_model_keywords[target_language]
    tts_lang_keyword = languages_tts_model_keywords[target_language]
    
    # Translation
    ta_sents = [english_text]
    translated = en2indic_model.batch_translate(ta_sents, 'en', target_lang_code)
    translated_str = ' '.join(translated)
    
    # PowerShell command to generate TTS
    command = [
        "powershell",
        "-ExecutionPolicy", "Bypass",
        "-File", ps1_file_path,
        translated_str,  # First argument
        gender,          # Second argument
        tts_lang_keyword, # Third argument
        output_file_path  # Fourth argument
    ]
    
    # Execute the PowerShell script
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True, encoding='utf-8')
        print("PowerShell script executed successfully.")
        print(result.stdout)  # Print the output of the script
        print(result.stderr)
    except subprocess.CalledProcessError as e:
        print(f"Error executing PowerShell script: {e}")
