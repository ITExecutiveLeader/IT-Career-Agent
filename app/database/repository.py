"""
Database repository operations.
"""

from sqlalchemy.orm import Session

from app.database.models import (
    Analysis,
    Resume,
    User,
)


def create_user(
    db: Session,
    email: str,
    display_name: str | None = None,
) -> User:
    """
    Create a new user.
    """

    user = User(
        email=email,
        display_name=display_name,
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


def get_user_by_email(
    db: Session,
    email: str,
) -> User | None:
    """
    Retrieve a user by email.
    """

    return (
        db.query(User)
        .filter(User.email == email)
        .first()
    )

def get_or_create_user(
    db,
    email: str,
    display_name: str,
):
    user = get_user_by_email(
        db,
        email,
    )

    if user:
        return user

    return create_user(
        db,
        email=email,
        display_name=display_name,
    )


def create_resume(
    db: Session,
    user_id: str,
    filename: str,
    raw_text: str,
) -> Resume:
    """
    Store a resume.
    """

    resume = Resume(
        user_id=user_id,
        filename=filename,
        raw_text=raw_text,
    )

    db.add(resume)
    db.commit()
    db.refresh(resume)

    return resume


def create_analysis(
    db: Session,
    user_id: str,
    job_description: str,
    report_content: str,
    ats_score: float | None = None,
    resume_id: str | None = None,
    job_title: str | None = None,
    matched_skills: str | None = None,
    missing_skills: str | None = None,
    recommendations: str | None = None,
) -> Analysis:
    """
    Store an analysis result.
    """

    analysis = Analysis(
        user_id=user_id,
        resume_id=resume_id,
        job_title=job_title,
        job_description=job_description,
        ats_score=ats_score,
        matched_skills=matched_skills,
        missing_skills=missing_skills,
        recommendations=recommendations,
        report_content=report_content,
    )

    db.add(analysis)
    db.commit()
    db.refresh(analysis)

    return analysis