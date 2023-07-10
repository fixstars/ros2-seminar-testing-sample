import pytest
from example_ament_python_pytest.add import add


def test_success():  # 成功するテスト
    assert add(1, 2) == 3


# def test_failure():  # 失敗するテスト
#     assert add(1, 2) == 4
