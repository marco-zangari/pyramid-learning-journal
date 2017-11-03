"""Doc string for __init__.py."""
from learning_journal.views.default import list_view, detail_view, create_view, update_view


def includeme(config):
    """Add views for each view and provide route name."""
    config.add_view(list_view, route_name='home')
    config.add_view(detail_view, route_name='journal')
    config.add_view(create_view, route_name='new-entry')
    config.add_view(update_view, route_name='edit-entry')
