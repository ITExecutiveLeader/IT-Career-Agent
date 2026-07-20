"""
Normalize extracted skill names to a canonical form.
"""

NORMALIZED_SKILLS = {

    # -------------------------
    # Cloud
    # -------------------------
    "microsoft azure": "azure",
    "azure cloud": "azure",
    "azure cloud services": "azure",
    "amazon web services": "aws",
    "aws cloud": "aws",

    "google cloud": "gcp",
    "google cloud platform": "gcp",

    # -------------------------
    # Containers
    # -------------------------
    "k8s": "kubernetes",

    # -------------------------
    # Source Control
    # -------------------------
    "github": "git",

    # -------------------------
    # Databases
    # -------------------------
    "sql server": "sql",
    "microsoft sql server": "sql",
    "ms sql": "sql",
    "postgres": "postgresql",

    # -------------------------
    # Microsoft / Identity
    # -------------------------
    "azure active directory": "azure ad",
    "entra": "entra id",
    "microsoft entra": "entra id",
    "office365": "office 365",
    "ms365": "microsoft 365",

    # -------------------------
    # Analytics / BI
    # -------------------------
    "powerbi": "power bi",

    # -------------------------
    # Security
    # -------------------------
    "multi factor authentication": "mfa",
    "multifactor authentication": "mfa",
    "two factor authentication": "2fa",
    "privileged access management": "pam",

    # -------------------------
    # Governance / Leadership
    # -------------------------
    "security governance": "it governance",
    "vendor & msp management": "vendor management",
    "vendor and msp management": "vendor management",
}


def normalize_skills(
    skills: list[str],
) -> list[str]:
    """
    Normalize extracted skill names.
    """

    normalized = []

    for skill in skills:

        skill = skill.lower().strip()

        skill = NORMALIZED_SKILLS.get(
            skill,
            skill,
        )

        if skill not in normalized:
            normalized.append(skill)

    return sorted(normalized)