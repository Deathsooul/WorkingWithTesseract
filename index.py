import pytesseract as ocr

from PIL import Image


phrase = ocr.image_to_string(Image.open('phrase.jpeg'), lang='por')
print(phrase)