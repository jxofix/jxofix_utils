import os
import sys
from pathlib import Path

from send2trash import send2trash

FOLDER_PATH = Path('/Users/Shared/OneDrive/Obrázky/01 Foto/2023/')
JPG_PATH = '/Users/Shared/OneDrive/Obrázky/01 Foto/2023/2023-05-20 Kanada/2023-10-21 Vessi urban photo/'


def walkthrough_subfolders(folder_path: Path = FOLDER_PATH):
    print(20*'*', 'Start', 20*'*')
    total_num = 0
    for subdir, dirs, files in os.walk(folder_path):
        if os.path.basename(subdir) == "RAW":
            cur_dir = Path(subdir)
            print(40*'-')
            print(5*'*', f"Deleting RAW in folder {cur_dir.parent}")
            deleted, num = deleteRAW(cur_dir.parent)
            total_num += num
            print('\n')

    print(2*'*', "Total deleted RAW: ", total_num)
    print(20 * '*', 'End', 20 * '*')

def deleteRAW(jpg_path: Path = JPG_PATH):
    """
    method to delete RAW files, if there is no relevant JPG or JPEG picture. e.g. 12345.ARW exist,
    but there is no 12345.JPG, the raw file will be deleted.

    :param jpg_path: path to folder where photos are stored
    :return: Count and list of deleted raw files
    """
    raw_path = os.path.join(jpg_path, "RAW")

    jpg_directory = os.fsencode(jpg_path)
    raw_directory = os.fsencode(raw_path)

    # store jpg files into array
    jpg_array = []
    deleted = []

    for file in os.listdir(jpg_directory):
        filename = os.fsdecode(file)
        if filename.endswith(".JPG") or filename.endswith(".JPEG"):
            name, extension = os.path.splitext(filename)
            jpg_array.append(name)

    # delete files which don't have corresponding jpg file
    for file in os.listdir(raw_directory):
        filename = os.fsdecode(file)
        raw_name, ext = os.path.splitext(filename)

        if raw_name not in jpg_array and (ext == ".ARW" or ext == ".DNG" or ext == ".CR2"):
            deleted.append(filename)
            send2trash(os.path.join(raw_path, filename))

    print(10*'*', f'Number of deleted photos: {len(deleted)}')
    print(10*'*', f'Deleted photos: {deleted}')
    return deleted, len(deleted)


if __name__ == '__main__':
    globals()[sys.argv[1]]()
