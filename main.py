from typing import Pattern
from src import adb
from src import list_music
import config
import sys, re

def main():
    android_ip: str = config.ANDROID_IP
    if len(sys.argv) > 1:
        
        have_wireless_option: bool = sys.argv[1] == '-w' or sys.argv[1] == '--wireless'
        if have_wireless_option:
            if len(sys.argv) != 3:
                raise Exception('MUST SPECIFY AN IP')
            IP_INDEX: int = 2
            re_ip: Pattern = re.compile(r'\d{3}\.\d{3}\.\d+\.\d+:\d{5}')
            is_valid_ip: bool = bool(re_ip.search( sys.argv[IP_INDEX] ))
        else:
            IP_INDEX: int = 1
            re_ip = re.compile(r'\d{3}\.\d{3}\.\d+\.\d+')
            is_valid_ip = bool(re_ip.search( sys.argv[IP_INDEX] ))

        if is_valid_ip:
            android_ip = sys.argv[IP_INDEX]
        else:
            raise Exception(f'el argumento "{sys.argv[IP_INDEX]}" no es una ip válida.')

    
    musics_in_folder: list[str] = list_music.get_musics_name(config.PC_MUSIC_FOLDER_PATH)
    adb.connect_to_device(config.ADB_EXECUTABLE_PATH, android_ip)
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

