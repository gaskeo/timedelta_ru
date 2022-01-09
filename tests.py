"""
Для запуска тестов необходимо:

- скачать и установить pytest:
    $ pip install pytest

- запустить тестирование:
    $ pytest tests.py
"""

from . import TimedeltaRu
from json import load


class TestStr:
    def test_str(self):
        """
        тест для метода __str__
        """
        with open("test_str.json", "r") as r:
            tests = load(r)
        for answer, data in tests:
            assert str(TimedeltaRu(**data)) == answer
