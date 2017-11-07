"""Set the default for the application."""

from pyramid.view import view_config
from learning_journal.data.data_entries import ENTRIES
from datetime import datetime
from pyramid.httpexceptions import HTTPNotFound, HTTPFound, HTTPBadRequest
from learning_journal.models.mymodel import Journal


@view_config(route_name='home', renderer='../templates/list.jinja2')
def list_view(request):
    """Create a home page."""
    entry = request.dbsession.query(Journal).all()
    if entry is None:
        raise HTTPNotFound
    return {"entries": entry}


@view_config(route_name='create', renderer='../templates/create.jinja2')
def create_view(request):
    """Create a new blog post."""
    return {"entries": ENTRIES}


@view_config(route_name='detail', renderer='../templates/detail.jinja2')
def detail_view(request):
    """Show single blog post."""
    entry_id = int(request.matchdict['id'])
    for entry in ENTRIES:
        if entry['id'] == entry_id:
            return {"entry": entry}


@view_config(route_name='update', renderer='../templates/update.jinja2')
def update_view(request):
    """Show single blog post."""
    return {"entries": ENTRIES}
