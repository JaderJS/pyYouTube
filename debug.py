import yt_dlp
import json


def download_audio(url, output_path="archives"):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(f"Download concluído para {url}")
    except Exception as e:
        print(f"Ocorreu um erro durante o download do vídeo {url}: {e}")


if __name__ == "__main__":
    with open("config.json", "r") as file:
        data = json.load(file)

    myUrls = data['urls']

for url in myUrls:
    download_audio(url)
