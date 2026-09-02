import re


def clean_text(text: str) -> str:
    """Clean and normalize resume text. """

    # 1. Convert to lowercase
    text = text.lower()

    # 2. Remove URLs
    text = re.sub(r"https?://\S+|www\.\S+"," ", text)

    # 3. Remove email addresses
    text = re.sub(r"\S+@\S+"," ", text)

    # 4. Convert ALL whitespace to a single space
    # Handles: \n, \t, multiple spaces
    text = re.sub(r"\s+"," ", text)

    # 5. Remove unwanted special characters
    text = re.sub(r"[^a-zA-Z0-9+#.\s]"," ", text)

    # 6. Normalize spaces again
    text = re.sub(r"\s+"," ", text)

    # 7. Remove leading/trailing spaces
    return text.strip()