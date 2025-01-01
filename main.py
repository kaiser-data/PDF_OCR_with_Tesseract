# git https://github.com/kaiser-data/PDF_OCR_with_Tesseract.git

from pdf2image import convert_from_path
from PIL import Image
import pytesseract
import os

# Path to tesseract executable (Optional, required if not in PATH)
pytesseract.pytesseract.tesseract_cmd = '/usr/local/bin/tesseract'  # Update if necessary


def pdf_to_text(pdf_path, output_folder='output_images', dpi=300):
    try:
        # Convert PDF to a list of images
        images = convert_from_path(pdf_path, dpi=dpi)

        # Create output folder if not exists
        os.makedirs(output_folder, exist_ok=True)

        extracted_text = ""

        # Process each page
        for i, image in enumerate(images):
            image_path = f"{output_folder}/page_{i + 1}.png"
            image.save(image_path, 'PNG')

            # OCR on each image
            text = pytesseract.image_to_string(image)
            extracted_text += text + "\n\n"

            print(f"Page {i + 1} done...")

        # Print the extracted text
        print("Extracted Text from PDF:")
        print(extracted_text)

        return extracted_text

    except Exception as e:
        print(f"Error: {e}")



if __name__ == "__main__":
    pdf_path = 'path_to_your_pdf/document.pdf'  # Replace with your PDF path
    pdf_to_text(pdf_path)
