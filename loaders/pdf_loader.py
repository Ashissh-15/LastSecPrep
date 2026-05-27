import fitz
import os

from loaders.table_extractor import extract_tables
from loaders.image_extractor import extract_image_description


def load_pdf(file_path):

    documents = []

    pdf = fitz.open(file_path)

    for page_number in range(len(pdf)):

        page = pdf[page_number]

        # -------------------------
        # Normal text extraction
        # -------------------------

        text = page.get_text().strip()

        if text:

            documents.append({
                "text": text,
                "source": file_path,
                "page": page_number + 1
            })

        # -------------------------
        # Image extraction + OCR
        # -------------------------

        try:

            images = page.get_images(full=True)

            for image_index, image in enumerate(images):

                xref = image[0]

                pix = fitz.Pixmap(pdf, xref)

                temp_image = (
                    f"temp_{page_number}_{image_index}.png"
                )

                # Convert CMYK if necessary
                if pix.n < 5:
                    pix.save(temp_image)

                else:
                    pix_rgb = fitz.Pixmap(
                        fitz.csRGB,
                        pix
                    )

                    pix_rgb.save(temp_image)

                    pix_rgb = None

                pix = None

                image_text=extract_image_description(
                    temp_image
                )

                if image_text.strip():

                    documents.append({

                        "text": image_text,

                        "source": file_path,

                        "page": page_number + 1
                    })

                # Remove temp image
                if os.path.exists(temp_image):
                    os.remove(temp_image)

        except Exception as e:

            print(
                f"Image extraction failed on page {page_number+1}: {e}"
            )


    # -------------------------
    # Table extraction
    # -------------------------

    try:

        tables = extract_tables(file_path)

        for table_index, table in enumerate(tables):

            if table.strip():

                documents.append({

                    "text": table,

                    "source": file_path,

                    "page": "table"
                })

    except Exception as e:

        print(
            f"Table extraction failed: {e}"
        )


    pdf.close()

    return documents