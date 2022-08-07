import subprocess

def connect_to_device(adb_executable_path: str, device_ip: str) -> None:
    """Connects with the devive of the if given in device_ip"""
    subprocess.run(fr'{adb_executable_path} kill-server')
    subprocess.run(fr'{adb_executable_path} start-server')
    subprocess.run(fr'{adb_executable_path} connect {device_ip}')
    print(f'Conectado satisfactoriamente a: {device_ip}')

def get_device_filenames(adb_executable_path, path_of_folder) -> list[str]:
    """Return a list with all the filenames in path_of_folder in the device"""
    files_in_device_byte: bytes = subprocess.check_output(fr'{adb_executable_path} shell ls {path_of_folder}')
    files_in_device: list[str] = files_in_device_byte.decode('utf-8').split('\r\r\n')
    return files_in_device

def send_files(adb_executable_path: str, files_to_send: list[str], path_of_send: str) -> None:
    """Send from pc the files given in files_to_send to path_of_send in the device connected.
    The function doesn verify if the file is in path_of_send"""

    for file in files_to_send:
        subprocess.run(fr'{adb_executable_path} push "{file}" "{path_of_send}"')
        print(f'enviado: {file}')
    print('se han enviado todos los archivos')
