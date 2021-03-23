from timedelta_rus import TimedeltaRus
from json import load


class TestStr:
    def test_str(self):
        """
        тест для метода __str__
        """
        with open("tests/test_str.json", "r") as r:
            tests = load(r)
        for answer, data in tests:
            assert str(TimedeltaRus(**data)) == answer


class TestDays:
    def test_days(self):
        """
        тест для метода get_days()
        """
        with open("tests/test_days.json", "r") as r:
            tests = load(r)
        for answer, data in tests:
            assert str(TimedeltaRus(**data).get_days()) == answer
