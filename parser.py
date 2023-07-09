import sys
from pathlib import Path

JPEG_IMAGES = []
JPG_IMAGES = []
PNG_IMAGES = []
MP4_VIDEO = []
MY_OTHERS = []


REGISTER_EXTENSION = {
    "JPEG": JPEG_IMAGES,
    "JPG": JPG_IMAGES,
    "PNG": PNG_IMAGES,
    "MP4": MP4_VIDEO,
}

FOLDERS = []
EXTENSION = set()
UNKNOWN = set()


def get_extension(filename: str) -> str:
    return Path(filename).suffix[1:].upper()


def scan(folder: Path) -> None:
    for item in folder.iterdir():
        if item.is_dir():
            if item.name not in ("JPG_IMAGES"):
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
    print(f"Images jpeg: {JPEG_IMAGES}")
