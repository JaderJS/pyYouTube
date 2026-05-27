import yt_dlp
import subprocess
import json
import os
import re

OUTPUT_DIR = "archives"

os.makedirs(OUTPUT_DIR, exist_ok=True)


def sanitize_filename(name):
    return re.sub(r'[\\/*?:"<>|]', "", name)


with open("config.json", "r") as file:
    data = json.load(file)

videos = data["videos"]

for item in videos:
    url = item["url"]
    start = item.get("from")
    end = item.get("to")

    try:
        print(f"Processando: {url}")

        ydl_opts = {
            "format": "bestaudio/best",
            "outtmpl": f"{OUTPUT_DIR}/%(title)s.%(ext)s",
            "quiet": False
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)

            title = sanitize_filename(info["title"])
            downloaded_file = ydl.prepare_filename(info)

        output_mp3 = os.path.join(
            OUTPUT_DIR,
            f"{title}.mp3"
        )

        ffmpeg_cmd = ["ffmpeg", "-y"]

        # seek rápido
        if start:
            ffmpeg_cmd.extend(["-ss", start])

        ffmpeg_cmd.extend([
            "-i",
            downloaded_file
        ])

        if end:
            ffmpeg_cmd.extend(["-to", end])

        ffmpeg_cmd.extend([
            "-vn",
            "-acodec", "libmp3lame",
            "-ab", "192k",
            output_mp3
        ])

        print("Convertendo para mp3...")
        subprocess.run(ffmpeg_cmd, check=True)

        os.remove(downloaded_file)

        print(f"Finalizado: {output_mp3}")

    except Exception as e:
        print(f"Erro no vídeo {url}: {e}")