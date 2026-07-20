from app.models import CareerContext


def test_context_defaults():

    context = CareerContext()

    assert context.resume is None
    assert context.job_description is None
    assert context.metadata == {}