import moviepy.editor as mp
import speech_recognition as sr
from datetime import timedelta
import sys
import os

def audio_chunks(source, recognizer, chunk_length=3):
    """Yield successive chunk_length segments of audio from the source."""
    while True:
        chunk = recognizer.record(source, duration=chunk_length)
        if not chunk.frame_data:
            break
        yield chunk

def write_srt(text, srt_file, chunk_length=3):
    """Convert transcription to SRT format based on 3-second intervals and write to a file."""
    lines = text.strip().split("\n")
    srt_format = ""
    start_time = timedelta(seconds=0)

    for i, line in enumerate(lines):
        if line.strip() == "NA":
            continue
        end_time = start_time + timedelta(seconds=chunk_length)
        srt_format += f"{i+1}\n"
        srt_format += f"{start_time} --> {end_time}\n"
        srt_format += f"{line.strip()}\n\n"
        start_time = end_time

    with open(srt_file, "w") as f:
        f.write(srt_format)
    print(f"SRT file has been created at {srt_file}")

def video_to_srt(video_path):
    wav = video_path.replace(".mp4", ".wav")
    srt = video_path.replace(".mp4", ".srt")

    try:
        # Extract audio from the video
        video = mp.VideoFileClip(video_path)
        video.audio.write_audiofile(wav)
        video.close()
    except Exception as e:
        print(f"Failed to extract audio: {e}")
        return

    r = sr.Recognizer()
    text = ""

    try:
        with sr.AudioFile(wav) as source:
            for audio_chunk in audio_chunks(source, r, chunk_length=3):
                try:
                    chunk_text = r.recognize_google(audio_chunk)
                    text += chunk_text + "\n"  # Changed to append a new line for each recognized chunk
                except sr.UnknownValueError:
                    text += "NA\n"  # Append "NA" followed by a new line for unavailable chunks
                except sr.RequestError as e:
                    print(f"API request failed: {e}")
                    text += "NA\n"  # Similarly for request errors
                print(len(text.strip().split()), "words transcribed")
    except Exception as e:
        print(f"Failed during speech recognition: {e}")
        return

    # Write to SRT file if transcription exists
    if text.strip():
        write_srt(text, srt, chunk_length=3)
    else:
        print("No transcription available.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <path_to_video_file>")
    else:
        video_path = sys.argv[1]
        video_to_srt(video_path)
        os.remove(video_path.replace(".mp4", ".wav"))  # Clean up temporary WAV file
