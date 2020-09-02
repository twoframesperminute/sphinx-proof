import shutil
from pathlib import Path

import pytest

from sphinx.testing.path import path

pytest_plugins = 'sphinx.testing.fixtures'

@pytest.fixture
def rootdir(tmpdir):
    src = path(__file__).parent.abspath() / "books"
    dst = tmpdir.join("books")
    shutil.copytree(src, dst)
    books = path(dst)
    yield books
    shutil.rmtree(dst)


