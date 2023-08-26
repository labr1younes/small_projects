from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS


# Reading the image from a path
def read_img(filepath):
    myimg = Image.open(filepath)
    return myimg


# Getting the most important data of the image
def get_basic_data(filepath):
    image = read_img(filepath)
    basic_data = {
        "Filename": image.filename,
        "Image Size": image.size,
        "Image Height": image.height,
        "Image Width": image.width,
        "Image Format": image.format,
        "Image Mode": image.mode
    }

    return basic_data


# Showing the most important data of the image
def print_basic_data(filepath):
    basic_data = get_basic_data(filepath)

    for key, value in basic_data.items():
        print(f"{key:25}: {value}")


# Getting the exif data of the image
def get_exif_data(filepath):
    image = read_img(filepath)
    exif_data = image.getexif()

    return exif_data


# Showing the exif data of the image
def print_exif_data(filepath):
    exif_data = get_exif_data(filepath)

    for tag_id in exif_data:
        tag = TAGS.get(tag_id, tag_id)
        data = exif_data.get(tag_id)
        # decode bytes
        if isinstance(data, bytes):
            data = data.decode()
        print(f"{tag:25}: {data}")


if __name__ == "__main__":

    path1= "Reconyx_HC500_Hyperfire.jpg"
    path2= "Canon_DIGITAL_IXUS_400.jpg"
    # img = Image.open(path)
    # metadata = img.getexif()

    print_basic_data(path2)
    print(len(TAGS),"\n------------------\n")
    print_exif_data(path2)

    # img.show()
