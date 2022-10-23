import os
from typing import NoReturn

from dotenv import load_dotenv


def pack(files_path: str, archive_name: str) -> NoReturn:
    '''Упаковывает файлы в архив'''
    cmd = f'zip -r - "{files_path}" > {archive_name}'
    os.system(cmd)


def main():
    load_dotenv()
    files_path = os.getenv('ARCHIVE_FILES_SAVE_PATH')
    archive_name = "first.zip"
    pack(files_path, archive_name)


if __name__ == '__main__':
    main()
