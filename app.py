# app.py
from flask import Flask, request, jsonify
import os
import sys
from pathlib import Path

app = Flask(__name__)

# Add paths
current_dir = Path(__file__).parent.absolute()
fairseq_path = current_dir / "fairseq"
indictrans_path = current_dir / "indicTrans"

# Add to Python path
sys.path.extend([str(fairseq_path), str(indictrans_path)])

# Initialize model (done only once when app starts)
def initialize_model():
    try:
        from indicTrans.inference.engine import Model
        model = Model(expdir=str(current_dir / "en-indic"))
        return model
    except Exception as e:
        print(f"Error initializing model: {e}")
        return None

# Initialize model at startup
translation_model = initialize_model()

@app.route('/translate', methods=['POST'])
def translate():
    try:
        data = request.get_json()
        
        if not data or 'text' not in data or 'target_lang' not in data:
            return jsonify({
                'error': 'Missing required fields. Please provide "text" and "target_lang"'
            }), 400
        
        text = data['text']
        target_lang = data['target_lang']
        
        # Ensure text is in list format as required by the model
        if isinstance(text, str):
            text = [text]
        
        # Perform translation
        if translation_model is None:
            return jsonify({'error': 'Model not initialized'}), 500
            
        translations = translation_model.batch_translate(text, 'en', target_lang)
        
        return jsonify({
            'source_text': text,
            'target_language': target_lang,
            'translations': translations
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)