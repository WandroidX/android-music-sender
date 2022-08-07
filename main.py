from src import adb
from src import list_music
import config
import sys, re

def main():
    IP: str = config.ANDROID_IP
    if len(sys.argv) == 2:
        re_ip = re.compile(r'\d{3}\.\d{3}\.\d\.\d{2}')
        if re_ip.search(sys.argv[2]):
            IP: str = sys.argv[2]
        else:
            raise Exception(f'el argumento "{sys.argv[2]}" no es una ip.')

    
    musics_in_folder: list[str] = list_music.get_musics_name(config.PC_MUSIC_FOLDER_PATH)
    adb.connect_to_device(config.ADB_EXECUTABLE_PATH, IP)
    files_in_device: list[str] = adb.get_device_filenames(
        config.ADB_EXECUTABLE_PATH, config.ANDROID_MUSIC_FOLDER_PATH
    )
    musics_in_device: list[str] = list(filter(lambda element: element.endswith('.mp3'), files_in_device))
    musics_to_send: list[str] = list(filter(lambda music: music not in musics_in_device, musics_in_folder))

    if musics_to_send:
        # here there the musics with her abs path
        abspath_musics_to_send: list[str] = list(map(lambda music: f'{config.PC_MUSIC_FOLDER_PATH}\\{music}', musics_to_send))
        adb.send_files(config.ADB_EXECUTABLE_PATH, abspath_musics_to_send, config.ANDROID_MUSIC_FOLDER_PATH )

if __name__ == '__main__':
    main()
else:
    print('Debe ser ejecutado como script')
