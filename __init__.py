from datetime import timedelta


class TimedeltaRu(timedelta):
    def __str__(self):
        english_time = super().__str__()
        dd = ""
        if "day" in english_time:
            dd = english_time.split()[0]

        time = english_time.split()[-1]
        if dd and dd.isdigit():
            days = self.__get_days(int(dd))
            return f"{days}, {time}"
        return time

    @staticmethod
    def __get_days(dd):
        """
        получить количество дней в формате 'n дней/дня/день'
        """
        ldd = dd % 10
        if (ldd == 0 or 5 <= ldd <= 9) or dd % 100 in {11, 12, 13, 14}:
            day = "дней"
        elif 2 <= ldd <= 4:
            day = "дня"
        else:
            day = "день"
        return f"{dd} {day}"


