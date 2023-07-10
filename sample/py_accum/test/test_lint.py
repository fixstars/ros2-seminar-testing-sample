# Copyright (c) 2023 Fixstars inc.
#
# Use of this source code is governed by an MIT-style
# license that can be found in the LICENSE file or at
# https://opensource.org/licenses/MIT.
import pytest

from ament_copyright.main import main as copyright_main
from ament_flake8.main import main_with_errors as flake8_main_with_errors
from ament_pep257.main import main as pep257_main


@pytest.mark.linter
@pytest.mark.copyright
def test_copyright():
    rc = copyright_main([])
    assert rc == 0, "Found errors"


@pytest.mark.linter
@pytest.mark.flake8
def test_flake8():
    rc, errors = flake8_main_with_errors([])
    assert rc == 0, f"Found {len(errors)} code style errors / warnings:\n" + "\n".join(
        errors
    )


@pytest.mark.linter
@pytest.mark.pep257
def test_pep257():
    rc = pep257_main([])
    assert rc == 0, "Found errors"
