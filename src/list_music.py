import os

def get_musics_name(path: str) -> list[str]:
    filelist: list[ str ] = os.listdir(path)
    return [
        filename for filename in filelist if filename.endswith('.mp3')
    ]
