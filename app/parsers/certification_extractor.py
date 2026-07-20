from .certification_catalog import CERTIFICATION_CATALOG


def extract_certifications(
    text: str,
) -> list[str]:
    """
    Extract certifications from text.
    """

    text = text.lower()

    found = []

    for certification in CERTIFICATION_CATALOG:

        if certification in text:
            found.append(certification)

    return sorted(found)