from PIL import Image, ImageDraw, ImageFont


def addNum(image):
    print('addNum')
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('/Library/Fonts/AppleMyungjo.ttf', 50)
    fillColor = '#ff0000'
    width, height = image.size
    draw.text((width - 70, 30), '99', font=font, fill=fillColor)
    image.save('result.jpg','jpeg')


if __name__ == '__main__':
    print(__file__)
    image = Image.open('./Totoro.jpeg')
    addNum(image)
    image.show()