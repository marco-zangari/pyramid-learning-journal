"""Set the default for the application."""

from pyramid.view import view_config
from learning_journal.data.data_entries import ENTRIES


@view_config(route_name='home', renderer='../templates/list.jinja2')
def list_view(request):
    """Create a home page."""
    return {"entries": ENTRIES}


@view_config(route_name='create', renderer='../templates/create.jinja2')
def create_view(request):
    """Create a new blog post."""
    return {"entries": ENTRIES}


@view_config(route_name='detail', renderer='../templates/detail.jinja2')
def detail_view(request):
    """Show single blog post."""
    entry_id = int(request.matchdict['id'])


    return {"entries": }


@view_config(route_name='update', renderer='../templates/update.jinja2')
def update_view(request):
    """Show single blog post."""
    return {"entries": ENTRIES}
