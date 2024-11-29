from flask import Flask, request, jsonify
from main import translate_and_generate_tts  # Import the function from main.py
from video_generation import get_pauses_in_audio, create_video_with_audio, wav_to_mp3

# Initialize the Flask app
app = Flask(__name__)

@app.route('/generate_video', methods=['POST'])
def generate_video():
    try:
        # Parse the JSON request
        data = request.json
        english_text = data['english_text']
        target_language = data['target_language']
        gender = data['gender']
        audio_file_path = data['audio_file_path']
        video_clip_file_path = data['video_clip_file_path']
        video_file_path = data['video_file_path']
        
        # Call the imported function
        # result = translate_and_generate_tts(
        #     english_text=english_text,
        #     target_language=target_language,
        #     gender=gender,
        #     output_file_path=audio_file_path
        # )

        audio_file_path = r'Fastspeech2_HS\\' + audio_file_path

        # Usage
        wav_to_mp3(audio_file_path, audio_file_path+".mp3")

        # Detect pauses in the audio
        pauses = get_pauses_in_audio(audio_file_path, silence_thresh=-40, min_silence_len=500)

        # Create video with pauses and audio
        try:
            create_video_with_audio(video_clip_file_path, audio_file_path, pauses, video_file_path)
            print(f"Final video saved to {video_file_path}")
        except Exception as e:
            print(f"Error: {e}")

        # Return the result as a JSON response
        return jsonify(result)
    
    except Exception as e:
        # Handle errors and return error response
        return jsonify({"status": "error", "message": str(e)}), 500
    
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
