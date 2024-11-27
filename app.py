from flask import Flask, request, jsonify
from main import translate_and_generate_tts  # Import the function from main.py

# Initialize the Flask app
app = Flask(__name__)

@app.route('/generate_tts', methods=['POST'])
def generate_tts():
    try:
        # Parse the JSON request
        data = request.json
        english_text = data['english_text']
        target_language = data['target_language']
        gender = data['gender']
        output_file_path = data['output_file_path']
        
        # Call the imported function
        result = translate_and_generate_tts(
            english_text=english_text,
            target_language=target_language,
            gender=gender,
            output_file_path=output_file_path
        )
        
        # Return the result as a JSON response
        return jsonify(result)
    
    except Exception as e:
        # Handle errors and return error response
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
