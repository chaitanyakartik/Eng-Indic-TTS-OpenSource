# from termcolor import colored
# import os
# import sys

# # Add the local fairseq directory to PYTHONPATH
# fairseq_path = r"E:\Projects\Multilingual_TTS\fairseq"  # Use raw string for Windows paths
# if fairseq_path not in sys.path:  # Ensure no duplicate entries
#     sys.path.append(fairseq_path)

# # Try importing Fairseq
# try:
#     from fairseq import checkpoint_utils,distributed_utils, options, tasks, utils
#     print(colored("Fairseq imported successfully!", "green"))  # Green text
# except Exception as e:
#     print(colored(f"Error during import: {e}", "red"))  # Red text
from translator_model import translator_model


# from indicTrans.inference.engine import Model

# en2indic_model = Model(expdir='E:\Projects\Multilingual_TTS\en-indic')
en2indic_model = translator_model(enindic_path="E:\Projects\Multilingual_TTS\en-indic",
                                         fairseq_path="E:\Projects\Multilingual_TTS\fairseq",
                                         indicTrans_path="E:\Projects\Multilingual_TTS\indicTrans")

ta_sents = ['In Nashik district’s Nandgaon constituency, scuffle broke out between Eknath Shinde-led Shiv Sena candidate Suhas Kande and Independent candidate Sameer Bhujbal, nephew of top NCP (Ajit Pawar) leader Chaggan Bhujbal at a polling centre']


translated = en2indic_model.batch_translate(ta_sents, 'en', 'hi')

print(translated)

