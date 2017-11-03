# -*- coding: utf-8 -*-
"""Test default.py."""
from __future__ import unicode_literals
from pyramid import testing
import pytest


from learning_journal.views.default import(
    list_view,
    detail_view,
    create_view,
    update_view,
)


@pytest.fixture
def list_view_fixture():
    """Make dummy request fixture."""
    lv = testing.DummyRequest()
    return list_view(lv)


# @pytest.fixture
# def dummy_request():
#     """Make dummy request fixture."""
#     return testing.DummyRequest()


# @pytest.fixture
# def dummy_request():
#     """Make dummy request fixture."""
#     return testing.DummyRequest()


# @pytest.fixture
# def dummy_request():
#     """Make dummy request fixture."""
#     return testing.DummyRequest()


def test_list_view_response_status_200(list_view_fixture):
    """Test the list_view function to return a status 200 OK."""
    response = list_view_fixture
    assert response.status_code == 200


# def test_detail_view_response_status_200(dummy_request):
#     """Test the detail_view function to return a status 200 OK."""
#     response = detail_view(dummy_request)
#     assert response.status_code == 200


# def test_create_view_response_status_200(dummy_request):
#     """Test the create_view function to return a status 200 OK."""
#     response = create_view(dummy_request)
#     assert response.status_code == 200


# def test_update_view_response_status_200(dummy_request):
#     """Test the update_view function to return a status 200 OK."""
#     response = update_view(dummy_request)
#     assert response.status_code == 200


# def test_list_view_response_text_has_proper_content_type(dummy_request):
#     """Test that list_view returns content expected."""
#     response = list_view(dummy_request)
#     import pdb; pdb.set_trace()
#     assert response.content_type == 'text/html'
