from PIL import Image
import glob
import os

def img_name(img):
    return img.filename

def img_foramt(img):
    return img.format

def img_dim(img):
    return img.size

def img_w(img):
    return img.width

def img_h(img):
    return img.height

def img_mod(img):
    return img.mode

def img_info(img):
    return img.info

def img_read(path):
    img = Image.open(path)
    return img

def img_size(path):
    size = os.stat(path).st_size
    size = round(size / 1024, 3)
    return size  

def to_rgp(img):
    img_RGB = img.convert('RGB')
    return img_RGB
    
def img_summery(path):
    img = img_read(file)
    print("Image Name        : {} ".format(img_name(img)))
    print("Image Format      : {} ".format(img_foramt(img)))
    print("Image Dimentions  : {} ".format(img_dim(img)))
    print("Image Size        : {} KB ".format(img_size(path)))
    print("Image Mode        : {} ".format(img_mod(img)))
    #print("Image Information : {} ".format(img_info(img)))
    
def png_2_jpg(path):
    img = img_read(path)
    img_new = to_rgp(img)
    img_new.save(path.replace("png", "jpg"), quality=99)
    print("Convert is done")

def jpg_2_png(path):
    img = img_read(path)
    img_new = to_rgp(img)
    img_new.save(path.replace("jpg", "png"), quality=95)
    print("Convert is done")
    
    


if __name__ == "__main__":
    for file in glob.glob("*.jpg"):
        jpg_2_png(file)
        img_summery(file)
        print("----------")
        
    print("done")
    

