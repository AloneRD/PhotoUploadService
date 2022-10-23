import os
from subprocess import check_output
from typing import NoReturn

from dotenv import load_dotenv


def save_file(byte_archive: bytes, archive_name:str) -> NoReturn:
    '''Сохраняет заархивированные данные в файл'''
    with open('archive.zip', 'wb') as archive:
        archive.write(byte_archive)


def pack(files_path: str, archive_name: str) -> NoReturn:
    '''Упаковывает файлы в архив'''
    archive = check_output(['zip', '-r', '-', files_path])
    save_file(archive, archive_name)


def main():
    load_dotenv()
    files_path = os.getenv('ARCHIVE_FILES_SAVE_PATH')
    archive_name = "first.zip"
    pack(files_path, archive_name)


if __name__ == '__main__':
    main()
