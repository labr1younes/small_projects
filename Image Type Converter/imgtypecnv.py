from PIL import Image
import glob
import os
import argparse

# Reading the image from a path
def img_read(path):
    img = Image.open(path)
    return img

# The image size in KB
def img_size(path):
    size = os.stat(path).st_size
    size = round(size / 1024, 3)
    return size

# Converting image to RGB 
def to_rgp(img):
    img_RGB = img.convert('RGB')
    return img_RGB

# Printing a small description about thet image  
def img_summery(path):
    img = img_read(path)
    print("Image Name        : {} ".format(img.filename))
    print("Image Format      : {} ".format(img.format))
    print("Image Dimentions  : {} ".format(img.size))
    print("Image Size        : {} KB ".format(img_size(path)))
    print("Image Mode        : {} ".format(img.mode))
    
# Converting image from png to jpg
def png_2_jpg(path):
    img = img_read(path)
    img_new = to_rgp(img)
    img_new.save(path.replace("png", "jpg"), quality=99)
    #print("Convert is done")
    
# Converting image from jpg to png
def jpg_2_png(path):
    img = img_read(path)
    img_new = to_rgp(img)
    img_new.save(path.replace("jpg", "png"), quality=99)
    #print("Convert is done")
    
# Preparing the parser
def prs():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d","--directory" ,required=True, help="specify the directory that contains the images ")
    parser.add_argument("-o","--option" , required=True,help="1 for (png->jpg) and 2 for (jpg->png)")
    
    args = parser.parse_args()
    return args

# Checking if the user's option input is valid 
def is_valid_option(op):
    if op.isdigit():
        o = int(op)
        if o in [1,2]:
            return True
        else:
            print("Choose [1] or [2] only")
            return False
    else:
        print("Option must be a number")
        return False

# Cheking if the user's directory input is valid
def is_valid_dir(path):
    if os.path.isdir(path):
        return True
    else:
        print("Path isn't corretct")
        return False
    
# Converting all the Images in the directory     
def cnvrt(a):
    tmp = str(a.directory)
    option = int(a.option)
    
    if option == 1:
        tmp += "\*.png"
        for file in glob.glob(tmp):
            png_2_jpg(file)
            print("- ", os.path.basename(file))
            #img_summery(file)
    elif option == 2:
        tmp += "\*.jpg"
        for file in glob.glob(tmp):
            jpg_2_png(file)
            print("- ", os.path.basename(file))
            #img_summery(file)
    print("\n------ All Converting is done")


if __name__ == "__main__":
    args = prs()
    
    if is_valid_option(args.option) and is_valid_dir(args.directory):      
        cnvrt(args)
    else:
        print("\n Convert Failed")
    
