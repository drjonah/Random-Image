import os, random
from PIL import Image, ImageFile

# global variables #
FOLDER_PATH = ""
VALID_IMAGE = ["png", "jpeg"]
ImageFile.LOAD_TRUNCATED_IMAGES = True

def filter_folder(folder: list) -> list:
    for file_name in folder:
        if file_name.split(".")[-1] not in VALID_IMAGE: folder.remove(file_name) 
    return folder

def main() -> None:
    # folder
    folder = filter_folder(os.listdir(FOLDER_PATH))
    # number of images in folder
    image_name = random.choice(folder)
    image_path = FOLDER_PATH + "/" + image_name
    # open image
    try:
        image = Image.open(image_path)
        image.show()
        print(f"OPENED:\n{image_name}\n{image_path}")
    except:
        print(f"ERROR:\n{image_name}\n{image_path}")

if __name__ == "__main__":
    main()
