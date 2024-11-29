import requests
from moviepy.editor


# url = "http://127.0.0.1:5000/generate_tts"
# data = {
#     "english_text": "However, LinkedIn defenders argue that the platform provides valuable opportunities for career advancement, networking, and industry insights. For many users, LinkedIn serves as a critical tool for building connections and accessing job opportunities in an increasingly competitive global job market.",
#     "target_language": "Hindi",
#     "gender": "male",
#     "output_file_path": "output6.wav"
# }

url = "http://127.0.0.1:5000/generate_video"
data = {
    "english_text": "However, LinkedIn defenders argue that the platform provides valuable opportunities for career advancement, networking, and industry insights. For many users, LinkedIn serves as a critical tool for building connections and accessing job opportunities in an increasingly competitive global job market.",
    "target_language": "Hindi",
    "gender": "male",
    "audio_file_path": "output6.wav",
    "video_clip_file_path": "inputs\vid.mp4",
    "video_file_path": "inputs\generated_video.mp4"
}

response = requests.post(url, json=data)
print(response.json(), flush=True)
