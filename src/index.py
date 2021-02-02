import pytesseract
import pdf2image
from PIL import Image


def pdfToImg(pdfFile):
    return pdf2image.convert_from_path(pdfFile)

def ocrCore(file):
    text = pytesseract.image_to_string(file)
    return text

def printPdf(pdfFile):
    imagem= pdfToImg(pdfFile)
    for pg, img in enumerate(imagem):
        print(ocrCore(img))

#Teste
printPdf('../src/assets/doc.pdf')