import pytesseract
from PIL import Image
from ppadb.client import Client
import numpy as np

import io
from time import sleep


def skip(width, height):
    x = width * .75
    y = height * .84

    device.shell(f"input tap {x} {y}")

def download(width, height):
    x = width * .95
    y = height * .84
    # print(f"adb shell input tap {x} {y}")
    device.shell(f"input tap {x} {y}")
    # device.shell(f"input tap {x} {y}")
    
    sleep(1)
    x = width * .85
    y = height * .51
    device.shell(f"input tap {x} {y}")
    sleep(2)
    skip(width, height)
def crop_image(image, width, height):
    top = height / 1.8 
    bottom = top + (height/10) 
     
    cropped_img = image.crop((0, top, width, bottom)) 
    # im1.save('screen1.png', 'PNG')
    return cropped_img



adb = Client(host='127.0.0.1', port=5037)
devices = adb.devices()
if len(devices) == 0:
    print('no device attached')
    quit()
device = devices[0]
# device.shell('input touchscreen swipe 500 500 500 500')

def run():
    image = device.screencap()

    image = Image.open(io.BytesIO(image))
    width, height = image.size 
#write images
# with open('screen.png', 'wb') as f:
    # f.write(image)
# image = Image.open('screen.png')

# Setting the points for cropped image 

    im = crop_image(image, width, height)
    read = pytesseract.image_to_string(im)
    print(read)
    search = 'North Texas'
    if search in read or 'Clock' in read:
        print('donwload')
        download(width, height)
        return 1
    else:
        print('skip')
        skip(width, height)
        return 0

if __name__ == "__main__":
    count = 0 
    while count != 500:

        count += run()
        sleep(3)
        print(count)

# device.shell(f'input touchscreen swipe 500 500 500 500 {int(distance)}')
