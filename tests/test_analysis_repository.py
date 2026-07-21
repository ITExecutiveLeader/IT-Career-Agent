from app.database.database import (
    Base,
    SessionLocal,
    engine,
)

from app.database.repository import (
    create_analysis,
    get_analysis,
    get_all_analyses,
    delete_analysis,
    get_or_create_user,
)


def setup_module():
    Base.metadata.create_all(bind=engine)


def test_analysis_repository():

    db = SessionLocal()

    try:

        user = get_or_create_user(
            db,
            email="analysis_test@example.com",
            display_name="Analysis Test",
        )

        analysis = create_analysis(
            db,
            user_id=user.id,
            job_description="Python Developer",
            report_content="Test Report",
            ats_score=95,
        )

        loaded = get_analysis(
            db,
            analysis.id,
        )

        assert loaded is not None
        assert loaded.id == analysis.id

        analyses = get_all_analyses(db)

        assert len(analyses) > 0

        deleted = delete_analysis(
            db,
            analysis.id,
        )

        assert deleted is True

        assert (
            get_analysis(
                db,
                analysis.id,
            )
            is None
        )

    finally:
        db.close()