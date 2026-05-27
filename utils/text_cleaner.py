import re


def clean_text(text):

    # Remove excessive spaces/newlines
    text = re.sub(r"\s+", " ", text)

    # Remove repeated dots
    text = re.sub(r"\.+", ".", text)

    # Remove weird characters
    text = re.sub(r"[^\w\s.,!?():/-]", "", text)

    return text.strip()