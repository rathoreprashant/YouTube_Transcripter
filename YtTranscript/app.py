import os
import subprocess
from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import FileResponse
import yt_dlp

app = FastAPI()

# Temporary directory for storing files
DOWNLOADS_DIR = "/tmp"

def download_audio(url: str) -> str:
    """Download audio from YouTube using yt-dlp"""
    options = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(DOWNLOADS_DIR, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with yt_dlp.YoutubeDL(options) as ydl:
        info = ydl.extract_info(url, download=True)
        return f"{info['title']}.mp3"

def compress_audio(input_path: str, output_path: str, bitrate: str = "64k"):
    """Compress MP3 audio to a smaller size using ffmpeg"""
    subprocess.run([
        "ffmpeg", "-i", input_path, "-b:a", bitrate, output_path, "-y"
    ], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

@app.get("/download")
def download_compressed_audio(url: str = Query(..., description="YouTube video URL")):
    try:
        # Download
        original_filename = download_audio(url)
        input_path = os.path.join(DOWNLOADS_DIR, original_filename)

        # Compress
        compressed_filename = f"compressed_{original_filename}"
        compressed_path = os.path.join(DOWNLOADS_DIR, compressed_filename)
        compress_audio(input_path, compressed_path)

        # Respond with file
        return FileResponse(
            path=compressed_path,
            filename=compressed_filename,
            media_type="audio/mpeg"
        )

    except Exception as e:
        print("ERROR:", str(e))  # Helpful for Cloud Run logs
        raise HTTPException(status_code=500, detail=str(e))
