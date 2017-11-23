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


@pytest.fixture
def add_models(dummy_request):
    """Add a bunch of model instances to the database."""
    dummy_request.dbsession.add_all(ENTRIES_LIST)


@pytest.fixture(scope="session")
def testapp(request):
    from webtest import TestApp
    from learning_journal import main

    app = main({}, **{"sqlalchemy.url": "postgres:///test_entries"})
    testapp = TestApp(app)

    SessionFactory = app.registry["dbsession_factory"]
    engine = SessionFactory().bind
    Base.metadata.create_all(bind=engine)

    def tearDown():
        Base.metadata.drop_all(bind=engine)

    request.addfinalizer(tearDown)

    return testapp


@pytest.fixture
def fill_the_db(testapp):
    SessionFactory = testapp.app.registry["dbsession_factory"]
    with transaction.manager:
        dbsession = get_tm_session(SessionFactory, transaction.manager)
        dbsession.add_all(ENTRIES)

    return dbsession