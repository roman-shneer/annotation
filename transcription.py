import pytesseract
from PIL import Image

# Set the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Update this path if necessary

# Load the image from which you want to extract text
image_path = 'trans.jpg'  # Replace with your image path
image = Image.open(image_path)

# Perform OCR on the image
transcribed_text = pytesseract.image_to_string(image)

# Print the transcribed text
print("Transcribed Text:")
print(transcribed_text)