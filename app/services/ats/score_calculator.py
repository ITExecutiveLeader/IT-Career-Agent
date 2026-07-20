from app.models import ATSResult

from .skill_weights import SKILL_WEIGHTS


class ScoreCalculator:
    """
    Calculates weighted ATS job match score.
    """

    def calculate(
        self,
        result: ATSResult,
    ) -> float:

        required_skills = (
            result.matched_skills
            +
            result.missing_skills
        )

        if not required_skills:
            result.overall_score = 0.0
            return 0.0

        total_weight = 0
        matched_weight = 0

        for skill in required_skills:

            weight = SKILL_WEIGHTS.get(
                skill.lower(),
                1,
            )

            total_weight += weight

            if skill in result.matched_skills:
                matched_weight += weight

        score = (
            matched_weight
            /
            total_weight
        ) * 100

        result.overall_score = round(
            score,
            2,
        )

        return result.overall_score