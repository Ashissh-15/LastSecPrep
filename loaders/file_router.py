import os

from loaders.pdf_loader import load_pdf
from loaders.docx_loader import load_docx
from loaders.pptx_loader import load_pptx


def load_file(file_path):

    extension = os.path.splitext(file_path)[1].lower()

    if extension == ".pdf":
        return load_pdf(file_path)

    elif extension == ".docx":
        return load_docx(file_path)

    elif extension == ".pptx":
        return load_pptx(file_path)

    else:
        print(f"Unsupported file type: {file_path}")
        return []