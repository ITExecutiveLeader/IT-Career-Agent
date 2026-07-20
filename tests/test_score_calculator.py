from app.models import ATSResult
from app.services.ats.score_calculator import ScoreCalculator


def test_score_calculator():

    result = ATSResult(
        matched_skills=[
            "python",
            "aws",
            "docker",
        ],
        missing_skills=[
            "terraform",
        ],
    )

    calculator = ScoreCalculator()

    score = calculator.calculate(
        result
    )

    assert score == 75.0

    assert result.overall_score == 75.0