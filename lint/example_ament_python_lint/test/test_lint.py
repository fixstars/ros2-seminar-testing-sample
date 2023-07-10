import pytest

from ament_flake8.main import main_with_errors as flake8_main_with_errors
from ament_xmllint.main import main as xmllint_main


@pytest.mark.linter
@pytest.mark.xmllint
def test_xmlint():
    rc = xmllint_main([])
    assert rc == 0, "Found errors"


@pytest.mark.linter
@pytest.mark.flake8
def test_flake8():
    rc, errors = flake8_main_with_errors([])
    assert rc == 0, f"Found {len(errors)} code style errors / warnings:\n" + "\n".join(
        errors
    )
