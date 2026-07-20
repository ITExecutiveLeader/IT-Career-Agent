from app.database.database import (
    Base,
    engine,
    SessionLocal,
)

from app.database.repository import (
    create_analysis,
    create_resume,
    get_or_create_user,
    get_user_by_email,
)


def setup_module():

    Base.metadata.create_all(
        bind=engine
    )


def test_database_workflow():

    db = SessionLocal()

    try:
        user = get_or_create_user(
            db,
            email="test@example.com",
            display_name="Test User",
        )

        assert user.id is not None


        found_user = get_user_by_email(
            db,
            "test@example.com",
        )

        assert found_user is not None


        resume = create_resume(
            db,
            user_id=user.id,
            filename="resume.pdf",
            raw_text="Python AWS Docker",
        )

        assert resume.id is not None


        analysis = create_analysis(
            db,
            user_id=user.id,
            resume_id=resume.id,
            job_description="Cloud Engineer",
            report_content="Analysis report",
            ats_score=92.5,
            matched_skills="python, aws",
            missing_skills="kubernetes",
            recommendations="Add Kubernetes experience",
        )

        assert analysis.id is not None
        assert analysis.ats_score == 92.5

    finally:
        db.close()