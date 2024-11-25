#import sys
#sys.path.append(r"E:\Projects\Multilingual_TTS\indicTrans\inference")
# test_import.py
try:
    from indicTrans.inference.custom_interactive import Translator
    print("Import successful!")
except Exception as e:
    print(f"Error during import: {e}")
