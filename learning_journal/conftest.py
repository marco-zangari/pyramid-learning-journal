# -*- coding: utf-8 -*-
"""Conftest where testing features interact with tests.py."""

import pytest
from pyramid import testing
import transaction
from learning_journal.models import (
    Journal,
    get_tm_session,
)
from learning_journal.models.meta import Base

@pytest.fixture(scope="session")
def configuration(request):
