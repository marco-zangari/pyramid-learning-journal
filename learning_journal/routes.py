"""View and connect all the routes."""


def includeme(config):
    """View the route for each view."""
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('list_view', '/')
    config.add_route('detail_view', '/journal/{id:\d+}')
    config.add_route('create_view', '/journal/new_entry')
    config.add_route('update_view', '/{id:\d+}/edit_entry')
