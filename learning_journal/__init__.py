from pyramid.config import Configurator
import os

def main(global_config, **settings):
    """Return a Pyramid WSGI application."""
    settings['sqlalchemy.url'] = os.environ.get('DATABASE_URL')
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.include('.routes')
    config.include('.models')
    config.add_static_view(name='static', path='learning_journal:static')
    config.scan()
    return config.make_wsgi_app()
