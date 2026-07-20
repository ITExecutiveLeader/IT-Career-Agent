import pytest

from app.database.database import SessionLocal
from app.database.models import (
    User,
    Resume,
    Analysis,
)


@pytest.fixture
def clean_database():

    db = SessionLocal()

    yield db

    db.query(Analysis).delete()
    db.query(Resume).delete()
    db.query(User).delete()

    db.commit()

    db.close()