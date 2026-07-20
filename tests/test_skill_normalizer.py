from app.parsers.skill_normalizer import normalize_skills


def test_skill_normalization():

    skills = [
        "Microsoft Azure",
        "Azure Cloud",
        "K8s",
        "MS SQL",
        "GitHub",
    ]

    normalized = normalize_skills(
        skills
    )

    assert "azure" in normalized

    assert "kubernetes" in normalized

    assert "sql" in normalized

    assert "git" in normalized

    assert len(normalized) == 4