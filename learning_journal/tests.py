# -*- coding: utf-8 -*-
"""Test default.py."""
from __future__ import unicode_literals
from pyramid import testing
from learning_journal.data.data_entries import ENTRIES
import pytest


from learning_journal.views.default import (
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


def test_list_view():
    """Test that what's returned by the view is a dictionary of values."""
    request = testing.DummyRequest()
    info = list_view(request)
    assert isinstance(info, dict)


def test_list_view_returns_proper_amount_of_content():
    """Home view response has file content."""
    request = testing.DummyRequest()
    response = list_view(request)
    assert len(response['entries']) == len(ENTRIES)


# def test_list_view_response_status_200(list_view_fixture):
#     """Test the list_view function to return a status 200 OK."""
#     response = list_view_fixture
#     assert response.status_code == 200


# def test_detail_view_response_status_200(list_view_fixture):
#     """Test the detail_view function to return a status 200 OK."""
#     response = list_view_fixture
#     assert response.status_code == 200


# def test_create_view_response_status_200(list_view_fixture):
#     """Test the create_view function to return a status 200 OK."""
#     response = list_view_fixture
#     assert response.status_code == 200


# def test_update_view_response_status_200(list_view_fixture):
#     """Test the update_view function to return a status 200 OK."""
#     response = list_view_fixture
#     assert response.status_code == 200


# def test_list_view_response_text_has_proper_content_type(list_view_fixture):
#     """Test that list_view returns content expected."""
#     response = list_view_fixture
#     assert response.content_type == 'text/html'
