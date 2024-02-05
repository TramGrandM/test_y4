from io import BytesIO

import requests
from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
try:
    image_url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR-1LWBXFybehCV2wLeflqYSSMTr34_pdNihd7dvTTdltmXnj6Xkw66Vxw9eOx1Z9YO79A&usqp=CAU'
    response = requests.get(image_url)
    img = Image.open(BytesIO(response.content))
    captcha_text = pytesseract.image_to_string(img)
except Exception as e:
    print("ERR:", e)
else:
    print("Captcha Text:", captcha_text)
finally:
    print("Convert captcha successfully")
