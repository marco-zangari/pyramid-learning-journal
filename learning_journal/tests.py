"""Test default.py."""
from pyramid import testing
import pytest


from learning_journal.views.default import(
    list_view,
    detail_view,
    create_view,
    update_view,
)


@pytest.fixture
def dummy_request():
    """Make dummy request fixture."""
    return testing.DummyRequest()


def test_list_view_response_status_200(dummy_request):
    """Test the list_view function to return a status 200 OK."""
    response = list_view(dummy_request)
    assert response.status_code == 200


def test_detail_view_response_status_200(dummy_request):
    """Test the list_view function to return a status 200 OK."""
    response = list_view(dummy_request)
    assert response.status_code == 200


def test_create_view_response_status_200(dummy_request):
    """Test the list_view function to return a status 200 OK."""
    response = list_view(dummy_request)
    assert response.status_code == 200


def test_list_update_response_status_200(dummy_request):
    """Test the list_view function to return a status 200 OK."""
    response = list_view(dummy_request)
    assert response.status_code == 200