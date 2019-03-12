import os
import shutil

from PIL import Image

ext = ['jpg', 'jpeg', 'png']


def copyImg():
    dst = 'temp_img'
    src = '/Users/kahn/Dev/my/Flutter/myworkspace/Flutter/flutter_app/images'

    # if not os.path.exists(dst):
    #     os.mkdir(dst)

    if os.path.exists(src) and not os.path.exists(dst):
        shutil.copytree(src, dst)


def copyAndProcess():
    copyImg()

    os.chdir('temp_img')
    files = os.listdir('.')
    for file in files:
        process_image(file)


def process_image(filename, mwidth=640, mheight=1136):
    image = Image.open(filename)
    w, h = image.size
    if w <= mwidth and h <= mheight:
        print(filename, 'is OK.')
        return
    if 1.0 * w / mwidth > 1.0 * h / mheight:
        scale = 1.0 * w / mwidth
        new_im = image.resize((int(w / scale), int(h / scale)), Image.ANTIALIAS)
    else:
        scale = 1.0 * h / mheight
        new_im = image.resize((int(w / scale), int(h / scale)), Image.ANTIALIAS)
    new_im.save('new-' + filename)
    new_im.close()


if __name__ == '__main__':
    print('0005')
    copyAndProcess()
    # process_image()
