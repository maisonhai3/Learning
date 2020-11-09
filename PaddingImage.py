import numpy as np
from PIL import Image, ImageDraw, ImageFont

mode = 'RGB'
tuple_sizeImgPadding = (150, 150)
tuple_sizeImgCharacter = (128, 128)
img_padding = Image.new(mode, tuple_sizeImgPadding, color='pink')
img_character = Image.new(mode, tuple_sizeImgCharacter, color='white')

img_padding.paste(img_character, (20, 20))
# img_padding.show('Image of Character')

# Drawing texts
image_im = Image.new(mode, tuple_sizeImgPadding, color='white')

drawing = ImageDraw.Draw(image_im)
drawing.text((20, 20), 'Hello there', fill='purple')

drawing = ImageDraw.Draw(image_im)
drawing.text((40, 40), 'I love you', fill='red')

font = ImageFont.truetype(font='arial.ttf', size=10)
drawing.text((60, 60), 'very much', fill='pink', font=font)
# image_im.show()
Image._show(image_im)