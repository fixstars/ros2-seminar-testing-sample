import pytest


def add(a, b):  # 簡略化のためここに書いている
    return a + b


def test_success():  # 成功するテスト
    assert add(1, 2) == 3


# def test_failure():  # 失敗するテスト
#     assert add(1, 2) == 4
