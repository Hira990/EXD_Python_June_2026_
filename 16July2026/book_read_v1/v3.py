import easyocr

# Initialize the reader (English)
reader = easyocr.Reader(['en'])

# Read text
result = reader.readtext("image.png")

for detection in result:
    bbox, text, confidence = detection
    print(f"Text: {text}")
    print(f"Confidence: {confidence:.2f}")