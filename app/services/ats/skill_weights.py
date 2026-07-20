"""
Skill weighting model for ATS matching.

Weights represent importance of a skill
when evaluating job fit.
"""

SKILL_WEIGHTS = {

    # -------------------------
    # Executive Leadership
    # -------------------------
    "it strategy": 5,
    "technology strategy": 5,
    "enterprise architecture": 5,
    "digital transformation": 5,
    "it governance": 5,
    "vendor management": 5,
    "operating model": 5,
    "stakeholder management": 5,
    "change management": 4,

    # -------------------------
    # Security / Compliance
    # -------------------------
    "cissp": 5,
    "zero trust": 5,
    "iam": 5,
    "incident response": 5,
    "siem": 4,
    "nist": 4,
    "iso 27001": 4,
    "soc 2": 4,
    "hipaa": 4,
    "mfa": 3,
    "2fa": 3,

    # -------------------------
    # Cloud / Infrastructure
    # -------------------------
    "aws": 4,
    "azure": 4,
    "docker": 3,
    "kubernetes": 3,
    "terraform": 3,
    "vmware": 3,
    "citrix": 3,
    "active directory": 3,

    # -------------------------
    # Data / Applications
    # -------------------------
    "sql": 3,
    "power bi": 3,
    "tableau": 3,
    "erp": 3,
    "business intelligence": 3,
    "data analytics": 3,

    # -------------------------
    # Development
    # -------------------------
    "python": 2,
    "java": 2,
    "javascript": 2,
    "c#": 2,
}