# Русификатор для `timedelta`
Библиотека с русской версией `__str__` для `datetime.timedelta`
      
### Использование
```
>>> from timedelta_ru import TimedeltaRu
>>> print(TimedeltaRu(days=117, seconds=6612))
117 дней, 1:50:12
>>> td_str = str(TimedeltaRu(days=12, seconds=612))
12 дней, 0:10:12
```

### Тестирование
#### pytest
Для тестирования используется библиотека [pytest](https://docs.pytest.org/en/6.2.x/)

Установка `pytest`:
```
$ pip install pytest
```

#### Команда для запуска
```
$ pytest tests.py
```

