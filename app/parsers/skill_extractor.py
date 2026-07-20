import re

from .skill_catalog import SKILL_CATALOG


def extract_skills(
    text: str,
) -> list[str]:
    """
    Extract known skills from text.
    """

    lower = text.lower()

    found = []

    for skill in sorted(SKILL_CATALOG):

        pattern = (
            r"\b"
            + re.escape(skill)
            + r"\b"
        )

        if re.search(pattern, lower):
            found.append(skill)

    from .skill_normalizer import normalize_skills

    return normalize_skills(found)