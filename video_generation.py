from pydub import AudioSegment
from pydub.silence import detect_silence
from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_videoclips

def get_pauses_in_audio(audio_file, silence_thresh=-40, min_silence_len=1000):
    """
    Detects pauses in an audio file and returns their timestamps.
    """
    audio = AudioSegment.from_file(audio_file)
    silence_ranges = detect_silence(audio, min_silence_len=min_silence_len, silence_thresh=silence_thresh)
    pause_timestamps = [(start / 1000.0, end / 1000.0) for start, end in silence_ranges]
    return pause_timestamps

def create_video_with_audio(video_file, audio_file, pauses, output_file):
    """
    Creates a video that loops the input video to match the audio length, inserts pauses in the video, and merges it with the audio.
    """
    # Load video and audio
    video = VideoFileClip(video_file)
    audio = AudioSegment.from_file(audio_file)
    audio_duration = len(audio) / 1000.0  # Convert to seconds

    # Loop the video to match the total audio duration
    loop_count = int(audio_duration / video.duration) + 1
    looped_video = concatenate_videoclips([video] * loop_count)
    looped_video = looped_video.subclip(0, audio_duration)

    # Create a silent segment for pauses
    silent_video = VideoFileClip(video_file).without_audio().subclip(0, video.duration).set_duration(0)

    # Insert pauses into the video based on detected timestamps
    video_clips = []
    previous_end = 0
    for start, end in pauses:
        # Add video segment before the pause
        if start > previous_end:
            video_clips.append(looped_video.subclip(previous_end, start))
        # Add silent video segment during the pause
        pause_duration = end - start
        silent_clip = silent_video.set_duration(pause_duration)
        video_clips.append(silent_clip)
        previous_end = end

    # Add the final part of the video if there's time left
    if previous_end < audio_duration:
        video_clips.append(looped_video.subclip(previous_end, audio_duration))

    # Concatenate all video parts
    final_video = concatenate_videoclips(video_clips)

    # Add the original audio to the final video
    final_audio = AudioFileClip(audio_file)
    final_video = final_video.set_audio(final_audio)

    # Export the final video
    final_video.write_videofile(output_file, codec="libx264", audio_codec="aac", fps=24)

import wave
import lameenc
import mutagen.mp3

def wav_to_mp3(wav_file, mp3_file):
    # Read the WAV file
    with wave.open(wav_file, 'rb') as wav:
        num_channels = wav.getnchannels()
        sample_width = wav.getsampwidth()
        sample_rate = wav.getframerate()
        num_frames = wav.getnframes()
        audio_data = wav.readframes(num_frames)

    # Encode to MP3
    encoder = lameenc.Encoder()
    encoder.set_bit_rate(192)          # Set bitrate (e.g., 192 kbps)
    encoder.set_in_sample_rate(sample_rate)
    encoder.set_channels(num_channels)
    encoder.set_quality(2)             # Set quality (0: highest, 9: lowest)

    mp3_data = encoder.encode(audio_data) + encoder.flush()

    # Write MP3 file
    with open(mp3_file, 'wb') as mp3:
        mp3.write(mp3_data)

    # Add metadata (optional)
    audio = mutagen.mp3.MP3(mp3_file)
    audio['TIT2'] = mutagen.id3.TIT2(encoding=3, text="Sample Title")  # Add Title
    audio.save()

    print("Conversion successful!")


