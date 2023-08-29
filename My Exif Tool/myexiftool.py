from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
import os


# Reading the image from a path
def read_img(filepath) -> Image :
    myimg = Image.open(filepath)
    return myimg


# Extracting from a filepath the image name , type and the folder path
def split_filepath(filepath):
    folder_path, full_filename = os.path.split(filepath)
    filename, file_extension = os.path.splitext(full_filename)
    return filename, file_extension, folder_path


# Getting the most important data of the image
def get_basic_data(filepath) -> dict:
    image = read_img(filepath)
    imagename = split_filepath(filepath)
    basic_data = {
        "Filename": imagename,
        "Image Size": image.size,
        "Image Height": image.height,
        "Image Width": image.width,
        "Image Format": image.format,
        "Image Mode": image.mode
    }

    return basic_data


# Showing the most important data of the image
def print_basic_data(filepath) -> None:
    basic_data = get_basic_data(filepath)

    for key, value in basic_data.items():
        print(f"{key:25}: {value}")


# Getting the exif data of the image
def get_exif_data(filepath):
    image = read_img(filepath)
    exif_data = image.getexif()
    if exif_data is None:
        return False
    else:
        return exif_data


# Showing the exif data of the image
def print_exif_data(filepath) -> None:
    exif_data = get_exif_data(filepath)
    if not exif_data:
        print(f"{filepath} doesn't have any Exif data ")
    else:
        for tag_id in exif_data:
            tag = TAGS.get(tag_id, tag_id)
            data = exif_data.get(tag_id)
            # decode bytes
            if isinstance(data, bytes):
                data = data.decode()
            print(f"{tag:25}: {data}")


# Removing the Exif data from the image
def rmv_exif_data(filepath :str) -> None:
    image = read_img(filepath)
    imagename, imagetype, imagepath = split_filepath(filepath)
    data = list(image.getdata())
    image2 = Image.new(image.mode, image.size)
    image2.putdata(data)
    complete_path = os.path.join(imagepath, f"{imagename}_noExif{imagetype}")
    image2.save(complete_path)


# Add one exif
def add_exif(newexif, tagnumber: int, value: str) -> None:
    newexif[tagnumber] = value
    # return newexif


# Add multiple exif
def add_mult_exif(newexif, exif_dic: dict) -> None:
    for tag, val in exif_dic.items():
        add_exif(newexif, tag, val)


if __name__ == "__main__":
    image = Image.open('Canon_DIGITAL_IXUS_400.jpg')

    # for i in TAGS:
    #     data = TAGS.get(i)
    #     # decode bytes
    #     if isinstance(data, bytes):
    #         data = data.decode()
    #     print(f"{data:25}: {i}")

    exif = image.getexif()
    exifnew = {
        271: 'hello',  # Date and time of the photo.
        9595: 'this',  # Camera make and model.
        1468: 'is  ',  # Camera make and model.
        2033: 'myexiftool',  # Camera make and model.
    }

    add_mult_exif(exif, exifnew)
    # add_exif(exif, 2020, "i dont know")

    # Save the image with the updated EXIF data.
    image.save('image_with_exif.jpg', exif=exif)
    print_exif_data('image_with_exif.jpg')


