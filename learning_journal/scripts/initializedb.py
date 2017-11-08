"""Initialize db module."""
import os
import sys
import transaction
from learning_journal.models.mymodel import Journal
from learning_journal.data.entry_data import ENTRIES
from datetime import datetime

from pyramid.paster import (
    get_appsettings,
    setup_logging,
)

from pyramid.scripts.common import parse_vars

from ..models.meta import Base
from ..models import (
    get_engine,
    get_session_factory,
    get_tm_session,
)
from ..models import Journal


def usage(argv):
    """Take one argument in usage."""
    cmd = os.path.basename(argv[0])
    print('usage: %s <config_uri> [var=value]\n'
          '(example: "%s development.ini")' % (cmd, cmd))
    sys.exit(1)


def main(argv=sys.argv):
    """Take one argument for main."""
    if len(argv) < 2:
        usage(argv)
    config_uri = argv[1]
    options = parse_vars(argv[2:])
    setup_logging(config_uri)
    settings = get_appsettings(config_uri, options=options)

    engine = get_engine(settings)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    session_factory = get_session_factory(engine)

    with transaction.manager:
        dbsession = get_tm_session(session_factory, transaction.manager)
        journal_models = []
        for entry in ENTRIES:
            new_entry = Journal(
                title=entry["title"],
                body=entry["body"],
                creation_date=datetime.now(),
            )
            journal_models.append(new_entry)
        dbsession.add_all(journal_models)
