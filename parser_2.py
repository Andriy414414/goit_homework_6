import sys
from pathlib import Path

JPEG_IMAGES = []
JPG_IMAGES = []
PNG_IMAGES = []
SVG_IMAGES = []
MP4_VIDEO = []
AVI_VIDEO = []
MKV_VIDEO = []
DOC_DOCS = []
DOCX_DOCS = []
PDF_DOCS = []
MP3_AUDIO = []
OGG_AUDIO = []
MY_OTHERS = []
ARCHIVES = []


REGISTER_EXTENSION = {
    "JPEG": JPEG_IMAGES,
    "JPG": JPG_IMAGES,
    "PNG": PNG_IMAGES,
    "SVG": SVG_IMAGES,
    "MP4": MP4_VIDEO,
    "AVI": AVI_VIDEO,
    "MKV": MKV_VIDEO,
    "DOC": DOC_DOCS,
    "DOCX": DOCX_DOCS,
    "PDF": PDF_DOCS,
    "MP3": MP3_AUDIO,
    "OGG": OGG_AUDIO,
    "ZIP": ARCHIVES
}

FOLDERS = []
EXTENSION = set()
UNKNOWN = set()

def get_extension(filename: str) -> str:
    return Path(filename).suffix[1:].upper()


def scan(folder: Path) -> None:
    # EXTENSION = set()
    # UNKNOWN = set()
    for item in folder.iterdir():
        if item.is_dir():
            if item.name not in ('archives', 'video', 'audio', 'documents', 'images', 'MY_OTHERS'):
                FOLDERS.append(item)
                scan(item)

            continue

        ext = get_extension(item.name)
        fullname = folder / item.name
        if not ext:
            MY_OTHERS.append(fullname)
        else:
            try:
                container = REGISTER_EXTENSION[ext]
                EXTENSION.add(ext)
                container.append(fullname)
            except KeyError:
                UNKNOWN.add(ext)
                MY_OTHERS.append(fullname)


if __name__ == "__main__":
    folder_to_scan = sys.argv[1]
    print(f"Start in folder {folder_to_scan}")
    scan(Path(folder_to_scan))
    print(f'Images jpeg: {JPEG_IMAGES}')
    print(f'Images jpg: {JPG_IMAGES}')
    print(f'Images png: {PNG_IMAGES}')
    print(f'Images svg: {SVG_IMAGES}')
    print(f'Video mp4: {MP4_VIDEO}')
    print(f'Video avi: {AVI_VIDEO}')
    print(f'Video mkv: {MKV_VIDEO}')
    print(f'Docs doc: {DOC_DOCS}')
    print(f'Docs docx: {DOCX_DOCS}')
    print(f'Docs pdf: {PDF_DOCS}')
    print(f'Audio mp3:{MP3_AUDIO}')
    print(f'Audio ogg:{OGG_AUDIO}')
    print(f'Archives: {ARCHIVES}')
    
    print(f'Types of files in folder: {EXTENSION}')
    print(f'Unknown files of types: {UNKNOWN}')
    print(f'MY_OTHER: {MY_OTHERS}')

    print(FOLDERS)



