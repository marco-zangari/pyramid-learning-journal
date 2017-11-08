# -*- coding: utf-8 -*-
"""Conftest where testing features interact with tests.py."""

import pytest
from pyramid import testing
import transaction
from learning_journal.models import (
    Journal,
    get_tm_session,
)
from learning_journal.models.meta import Base


@pytest.fixture(scope="session")
def configuration(request):
    """Set a configurator instance, e.g. a pointer to database."""
    config = testing.setUp(settings={
        'sqlalchemy.url': 'postgres:///test_entries'
})
    config.include("learning_journal.models")

    def teardown():
        """Set teardown of database."""
        testing.tearDown()
        request.addfinalizer(teardown)
        return config


@pytest.fixture
def db_session(configuration, request):
    """Create a session for interacting with the test database."""
    SessionFactory = configuration.registry["dbsession_factory"]
    session = SessionFactory()
    engine = session.bind
    Base.metadata.create_all(engine)

    def teardown():
        """Return new session with every request of dummy object."""
        session.transaction.rollback()
        Base.metadata.drop_all(engine)

    request.addfinalizer(teardown)
    return session


@pytest.fixture
def dummy_request(db_session):
    """Instantiate a fake HTTP Request, complete with a database session."""
    return testing.DummyRequest(dbsession=db_session)
