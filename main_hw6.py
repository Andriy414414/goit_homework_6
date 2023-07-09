from pathlib import Path
import shutil
import sys
import parser as parser
from normalize import normalize

def handle_media(filename: Path, target_folder: Path) -> None:
    target_folder.mkdir(exist_ok=True, parents=True)
    filename.replace(target_folder / normalize(filename.name))

def handle_docs(filename: Path, target_folder: Path) -> None:
    target_folder.mkdir(exist_ok=True, parents=True)
    filename.replace(target_folder / normalize(filename.name))

def handle_other(filename: Path, target_folder: Path) -> None:
    target_folder.mkdir(exist_ok=True, parents=True)
    filename.replace(target_folder / normalize(filename.name)) 

def handle_archive(filename: Path, target_folder: Path) -> None:
    target_folder.mkdir(exist_ok=True, parents=True)
    filename.replace(target_folder / normalize(filename.name))
    folder_for_file = target_folder / normalize(filename.name.replace(filename.suffix, ''))
    folder_for_file.mkdir(exist_ok=True, parents=True)
    try:
        shutil.unpack_archive(filename, folder_for_file)
    except shutil.ReadError:
        print("It is not archive")
        folder_for_file.rmdir()
    filename.unlink()

def handle_folder(folder: Path):
    try:
        folder.rmdir()
    except OSError:
        print(f"Can't delete folder: {folder}")

def main(folder: Path):
    parser.scan(folder)
    for file in parser.JPEG_IMAGES:
        handle_media(file, folder / 'images' / 'JPEG')
    for file in parser.JPG_IMAGES:
        handle_media(file, folder / 'images' / 'JPG')
    for file in parser.PNG_IMAGES:
        handle_media(file, folder / 'images' / 'PNG')
    for file in parser.SVG_IMAGES:
        handle_media(file, folder / 'images' / 'SVG')
    for file in parser.MP4_VIDEO:
        handle_media(file, folder / 'video' / 'MP4')
    for file in parser.AVI_VIDEO:
        handle_media(file, folder / 'video' / 'AVI')
    for file in parser.MKV_VIDEO:
        handle_media(file, folder / 'video' / 'MKV')
    for file in parser.DOC_DOCS:
        handle_docs(file, folder / 'docs' / 'DOC')
    for file in parser.DOCX_DOCS:
        handle_docs(file, folder / 'docs' / 'DOCX')
    for file in parser.PDF_DOCS:
        handle_docs(file, folder / 'docs' / 'PDF')
    for file in parser.OGG_AUDIO:
        handle_media(file, folder / 'audio' / 'OGG')
    for file in parser.MP3_AUDIO:
        handle_media(file, folder / 'audio' / 'MP3')
    for file in parser.MY_OTHERS:
        handle_media(file, folder / 'MY_OTHERS')
    for file in parser.ARCHIVES:
        handle_media(file, folder / 'ARCHIVES')

    for folder in parser.FOLDERS[::-1]:
        handle_folder(folder)

if __name__ == "__main__":
    if sys.argv[1]:
        folder_for_scan = Path(sys.argv[1])
        print(f'Start in folder: {folder_for_scan.resolve()}')
        main(folder_for_scan.resolve())
