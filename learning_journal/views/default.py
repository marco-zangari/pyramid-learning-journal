"""Set the default for the application."""

from pyramid.response import view_config
import io
import os

HERE = os.path.dirname(__file__)


@view_config(route_name='list_view', renderer='learning_journal:templates/list_view.jinja2')
def list_view(request):
    """Create a home page."""
    path = os.path.join(HERE, '../templates/list_view.html')
    with io.open(path) as imported_text:
        return Response(imported_text.read())


@view_config(route_name='create_view', renderer='learning_journal:templates/create_view.jinja2')
def create_view(request):
    """Create a new blog post."""
    path = os.path.join(HERE, '../templates/create_view.html')
    with io.open(path) as imported_text:
        return Response(imported_text.read())


@view_config(route_name='detail_view', renderer='learning_journal:templates/detail_view.jinja2')
def detail_view(request):
    """Show single blog post."""
    path = os.path.join(HERE, '../templates/detail_view.html')
    with io.open(path) as imported_text:
        return Response(imported_text.read())


@view_config(route_name='update_view', renderer='learning_journal:templates/update_view.jinja2')
def update_view(request):
    """Show single blog post."""
    path = os.path.join(HERE, '../templates/update_view.html')
    with io.open(path) as imported_text:
        return Response(imported_text.read())
