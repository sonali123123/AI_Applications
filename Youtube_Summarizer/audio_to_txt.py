
import os
import whisper
from pydub import AudioSegment

def process_uploaded_video(video_path: str, output_folder: str):
    os.makedirs(output_folder, exist_ok=True)
    
    # Convert the video to audio (mp3) using pydub
    audio = AudioSegment.from_file(video_path)
    mp3_path = os.path.join(output_folder, "audio.mp3")
    audio.export(mp3_path, format="mp3")

    return mp3_path

def transcribe_audio(audio_path: str, output_folder: str):
    whisper_model = whisper.load_model("base")
    try:
        result = whisper_model.transcribe(audio_path, language="english")
        transcription_text = result.get("text", "")
        os.makedirs(output_folder, exist_ok=True)
        transcription_filename = "audio_transcription.txt"
        transcription_path = os.path.join(output_folder, transcription_filename)
        with open(transcription_path, "w", encoding="utf-8") as f:
            f.write(transcription_text)
        return transcription_path
    except Exception as e:
        raise Exception(f"Failed to transcribe audio: {e}")
