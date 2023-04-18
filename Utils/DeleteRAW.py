import os
from send2trash import send2trash


def deleteRAW(jpg_path: str):
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

        if raw_name not in jpg_array and (ext == ".ARW" or ext == ".DNG"):
            deleted.append(filename)
            send2trash(os.path.join(raw_path, filename))

    return deleted, len(deleted)


if __name__ == '__main__':
    path = '/Users/Shared/OneDrive/Obrázky/01 Foto/2023/2023-03-08 Bolivia/2023-03-21 Valle de la luna, Animes/Foto/Sony'
    # path = '/Users/Shared/OneDrive/Obrázky/01 Foto/2022-10-19 Staromestka mostecka vez/'
    deleted_photos, num = deleteRAW(path)
    print(f'Number of deleted photos: {num}')
    print(f'Deleted photos: {deleted_photos}')

