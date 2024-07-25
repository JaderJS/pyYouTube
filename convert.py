import os
from pydub import AudioSegment


def convert_mp4_to_mp3(folder_path):
    # Verifica se o diretório existe
    if not os.path.exists(folder_path):
        print(f"O diretório {folder_path} não existe.")
        return

    # Itera sobre todos os arquivos no diretório
    for filename in os.listdir(folder_path):
        if filename.endswith(".mp4"):
            mp4_path = os.path.join(folder_path, filename)
            mp3_path = os.path.join(folder_path, os.path.splitext(filename)[0] + ".mp3")

            try:
                print(f"Convertendo {mp4_path} para {mp3_path}...")
                audio = AudioSegment.from_file(mp4_path, format="mp4")
                audio.export(mp3_path, format="mp3")
                print(f"Conversão concluída: {mp3_path}")
            except Exception as e:
                print(f"Erro ao converter {mp4_path}: {e}")


if __name__ == "__main__":
    folder_path = "archives"  # Altere para o caminho da sua pasta com arquivos MP4
    convert_mp4_to_mp3(folder_path)
