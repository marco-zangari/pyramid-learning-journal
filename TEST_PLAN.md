# Tests for Step 1

def test_list_view_response_status_200(list_view_fixture):
    """Test the list_view function to return a status 200 OK."""
    response = list_view_fixture
    assert response.status_code == 200


def test_detail_view_response_status_200(list_view_fixture):
    """Test the detail_view function to return a status 200 OK."""
    response = list_view_fixture
    assert response.status_code == 200


def test_create_view_response_status_200(list_view_fixture):
    """Test the create_view function to return a status 200 OK."""
    response = list_view_fixture
    assert response.status_code == 200


def test_update_view_response_status_200(list_view_fixture):
    """Test the update_view function to return a status 200 OK."""
    response = list_view_fixture
    assert response.status_code == 200


def test_list_view_response_text_has_proper_content_type(list_view_fixture):
    """Test that list_view returns content expected."""
    response = list_view_fixture
    assert response.content_type == 'text/html'


# Tests for Step 2

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


def test_detail_view():
    """Test that what's returned by the view is a dictionary of values."""
    request = testing.DummyRequest()
    request.matchdict['id'] = 13
    info = detail_view(request)
    assert isinstance(info, dict)


def test_detail_view_response_contains_entries_attrs():
    """Test that what's returned by the view contains one expense object."""
    request = testing.DummyRequest()
    request.matchdict['id'] = 13
    info = detail_view(request)
    for key in ["creation_date", "id", "body", "title"]:
        assert key in info['entry'].keys()


# Tests for Step 3

def test_model_gets_added(db_session):
    """Test the models are added to the database, as data_entries."""
    assert len(db_session.query(Journal).all()) == 0
    model = Journal(
        title="Some description text",
        body="Some longer description than in the title",
        creation_date=datetime.now(),
    )
    db_session.add(model)
    assert len(db_session.query(Journal).all()) == 1


def test_list_view_returns_dict(dummy_request):
    """Home view returns a dictionary of values."""
    from learning_journal.views.default import list_view
    response = list_view(dummy_request)
    assert isinstance(response, dict)


def test_list_view_returns_empty_when_database_empty(dummy_request):
    """List view returns nothing when there is no data."""
    from learning_journal.views.default import list_view
    response = list_view(dummy_request)
    assert len(response['entries']) == 0


def test_list_view_returns_count_matching_database(dummy_request):
    """Home view response matches database count."""
    from learning_journal.views.default import list_view
    response = list_view(dummy_request)
    query = dummy_request.dbsession.query(Journal)
    assert len(response['entries']) == query.count()


# Tests for Step 4
