from indicTrans.inference.engine import Model
from termcolor import colored
import os
import sys

def translator_model(enindic_path: str, fairseq_path: str,indicTrans_path: str) -> Model:

    #fairseq_path = r"E:\Projects\Multilingual_TTS\fairseq"  # Use raw string for Windows paths

    if fairseq_path not in sys.path:  # Ensure no duplicate entries
        sys.path.append(fairseq_path)

    #indic_path = 'E:\Projects\Multilingual_TTS\en-indic'

    #before i do this i need to cd into indicTrans
    os.chdir(indicTrans_path)
    en2indic_model = Model(expdir=enindic_path)


    return en2indic_model