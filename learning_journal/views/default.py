"""Set the default for the application."""

from pyramid.view import view_config
from learning_journal.data.entry_data import ENTRIES


@view_config(route_name='list_view', renderer='learning_journal:templates/list_view.jinja2')
def list_view(request):
    """Create a home page."""
    return {"entries": ENTRIES}


@view_config(route_name='create_view', renderer='learning_journal:templates/create_view.jinja2')
def create_view(request):
    """Create a new blog post."""
    return {"entries": ENTRIES}


@view_config(route_name='detail_view', renderer='learning_journal:templates/detail_view.jinja2')
def detail_view(request):
    """Show single blog post."""
    return {"entries": ENTRIES}


@view_config(route_name='update_view', renderer='learning_journal:templates/update_view.jinja2')
def update_view(request):
    """Show single blog post."""
    return {"entries": ENTRIES}
