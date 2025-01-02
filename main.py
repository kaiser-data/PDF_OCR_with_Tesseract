from pdf2image import convert_from_path
import pytesseract
import os

# Path to tesseract executable (Optional, required if not in PATH)
pytesseract.pytesseract.tesseract_cmd = '/opt/homebrew/bin/tesseract'  # Update if necessary


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
            custom_config = r'--psm 6 -l deu --oem 1'  # Ensure OCR Engine 1 (LSTM)
            text = pytesseract.image_to_string(image, config=custom_config)

            # Optional: Force UTF-8 encoding
            text = text.encode('utf-8').decode('utf-8')

            extracted_text += text + "\n\n"

            print(f"Page {i + 1} done...")

        # Print the extracted text
        print("Extracted Text from PDF:")
        print(extracted_text)

        return extracted_text

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    pdf_path = 'AZ_MK.pdf'
    pdf_to_text(pdf_path)
