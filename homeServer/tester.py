from PIL import Image
from PIL.ExifTags import TAGS
import requests
import wget

def get_exif(fn):
    ret = {}

    i = Image.open(fn)

    info = i._getexif()

    for tag, value in info.items():
        decoded = TAGS.get(tag,tag)
        ret[decoded] = value
    return ret



test_location ='file:///home/david/photo_images/IMG_1194.JPG'
file = wget.download(test_location)
tester = get_exif(test_location)