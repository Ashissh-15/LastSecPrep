from PIL import Image
import pytesseract
import os


pytesseract.pytesseract.tesseract_cmd=(
r"C:\Users\USER\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"
)

os.environ["TESSDATA_PREFIX"]=(
r"C:\Users\USER\AppData\Local\Programs\Tesseract-OCR\tessdata"
)


def extract_image_description(
    image_path
):

    try:

        try:

            img=Image.open(
                image_path
            )

        except Exception:

            # Skip unsupported formats
            return ""


        text=(
            pytesseract.image_to_string(
                img,
                lang="eng"
            )
        )

        return text.strip()


    except Exception:

        return ""