from pytube import YouTube
import json

with open("config.json", "r") as file:
    data = json.load(file)

myUrls = data['urls']


for url in myUrls:
    try:
        video = YouTube(url)
        print(f"Baixando áudio do vídeo {video.title}...")

        audio_stream = video.streams.filter(only_audio=True, progressive=True).first()

        if not audio_stream:
            print("Nenhum stream de áudio encontrado.")
            break

        # audio_stream.download(output_path="archives")
        print("Download concluído!")
        
    except Exception as e:
        print(f"Ocorreu um erro durante o download do vídeo {url}: {e}")
