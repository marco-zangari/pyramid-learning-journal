"""View and connect all the routes."""


def includeme(config):
    """View the route for each view."""
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('detail', '/journal/{id:\d+}')
    config.add_route('create', '/journal/new_entry')
    config.add_route('update', '/journal/{id:\d+}/edit_entry')
