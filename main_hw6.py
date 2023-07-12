from pathlib import Path
import shutil
import sys
import parser_2 as parser_2
from normalize import normalize

def handle_media(filename: Path, target_folder: Path) -> None:
    target_folder.mkdir(exist_ok=True, parents=True)
    filename.replace(target_folder / normalize(filename.name))

def handle_other(filename: Path, target_folder: Path) -> None:
    target_folder.mkdir(exist_ok=True, parents=True)
    filename.replace(target_folder / normalize(filename.name)) 

# def handle_archive(filename: Path, target_folder: Path) -> None:
#     target_folder.mkdir(exist_ok=True, parents=True)
#     filename.replace(target_folder / normalize(filename.name))
#     folder_for_file = target_folder / normalize(filename.name.replace(filename.suffix, ''))
#     folder_for_file.mkdir(exist_ok=True, parents=True)
#     try:
#         shutil.unpack_archive(filename, folder_for_file)
#     except shutil.ReadError:
#         print("It is not archive")
#         folder_for_file.rmdir()
#     filename.unlink()

def handle_archive(filename: Path, target_folder: Path) -> None:
    target_folder.mkdir(exist_ok=True, parents=True)
    filename = filename.replace(target_folder / normalize(filename.name))
    folder_for_file = target_folder / filename.stem
    folder_for_file.mkdir(exist_ok=True, parents=True)
    try:
        shutil.unpack_archive(filename, folder_for_file)
        filename.unlink()
    except shutil.ReadError:
        print("It is not archive")
        folder_for_file.rmdir()

def handle_folder(folder: Path):
    try:
        folder.rmdir()
    except OSError:
        print(f"Can't delete folder: {folder}")

def main(folder: Path):
    parser_2.scan(folder)
    for file in parser_2.JPEG_IMAGES:
        handle_media(file, folder / 'images' / 'JPEG')
    for file in parser_2.JPG_IMAGES:
        handle_media(file, folder / 'images' / 'JPG')
    for file in parser_2.PNG_IMAGES:
        handle_media(file, folder / 'images' / 'PNG')
    for file in parser_2.SVG_IMAGES:
        handle_media(file, folder / 'images' / 'SVG')
    for file in parser_2.MP4_VIDEO:
        handle_media(file, folder / 'video' / 'MP4')
    for file in parser_2.AVI_VIDEO:
        handle_media(file, folder / 'video' / 'AVI')
    for file in parser_2.MKV_VIDEO:
        handle_media(file, folder / 'video' / 'MKV')
    for file in parser_2.DOC_DOCS:
        handle_media(file, folder / 'documents' / 'DOC')
    for file in parser_2.DOCX_DOCS:
        handle_media(file, folder / 'documents' / 'DOCX')
    for file in parser_2.PDF_DOCS:
        handle_media(file, folder / 'documents' / 'PDF')
    for file in parser_2.OGG_AUDIO:
        handle_media(file, folder / 'audio' / 'OGG')
    for file in parser_2.MP3_AUDIO:
        handle_media(file, folder / 'audio' / 'MP3')
    for file in parser_2.MY_OTHERS:
        handle_media(file, folder)
    for file in parser_2.ARCHIVES:
        handle_archive(file, folder / 'archives')

    for folder in parser_2.FOLDERS[::-1]:
        handle_folder(folder)

if __name__ == "__main__":
    if sys.argv[1]:
        folder_for_scan = Path(sys.argv[1])
        print(f'Start in folder: {folder_for_scan.resolve()}')
        main(folder_for_scan.resolve())

