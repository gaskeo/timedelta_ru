from timedelta import TimedeltaRus


def test_den():
    """
    тест для 1 день
            21 день
            31 день...
    """
    for day in range(1, 502, 20):
        assert str(TimedeltaRus(days=day)) == f"{day} день, 0:00:00"


def test_dnei():
    """
    тест для 12 дней
             26 дней
             60 дней...
    """
    days = ((range(5, 21),) +
            tuple(range(x * 10 + 5, (x + 1) * 10 + 1) for x in range(2, 80)) +
            tuple(range(y * 100 + 10, y * 100 + 14) for y in range(1, 80)))
    for group in days:
        for day in group:
            assert str(TimedeltaRus(days=day)) == f"{day} дней, 0:00:00"


def test_dnya():
    """
    тест для 2 дня
            23 дня
            144 дня...
    """
    days = ((range(2, 5),) +
            tuple(range(x * 10 + 2, x * 10 + 5) for x in range(2, 80) if (x * 10 + 2) % 100 != 12))
    for group in days:
        for day in group:
            assert str(TimedeltaRus(days=day)) == f"{day} дня, 0:00:00"

