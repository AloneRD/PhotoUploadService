import asyncio
import os
from typing import NoReturn

from dotenv import load_dotenv


def save_file(byte_archive: bytes, archive_name:str) -> NoReturn:
    '''Сохраняет заархивированные данные в файл'''
    with open(archive_name, 'ab') as archive:
        archive.write(byte_archive)


async def pack(files_path: str, archive_name: str) -> NoReturn:
    '''Упаковывает файлы в архив'''
    cmd = f'zip -r - {files_path}'
    process = await asyncio.subprocess.create_subprocess_exec(
        'zip',
        '-r',
        '-',
        files_path,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )
    while  not process.stdout.at_eof(): 
        stdout = await process.stdout.read(100*1000)
        save_file(stdout, 'first.zip')


def main():
    load_dotenv()
    files_path = os.getenv('ARCHIVE_FILES_SAVE_PATH')
    archive_name = "first.zip"
    asyncio.run(pack(files_path, archive_name))


if __name__ == '__main__':
    main()
