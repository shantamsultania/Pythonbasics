import pytesseract
import cv2

im = cv2.imread('ocr2.jpeg')
pytesseract.pytesseract.tesseract_cmd =r'F:\ocr\tesseract.exe'
text = pytesseract.image_to_string(im, lang = 'eng')

print(text)
