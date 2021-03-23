from datetime import timedelta


class TimedeltaRus(timedelta):
    def __str__(self):
        mm, ss = self.seconds // 60, self.seconds % 60
        mm, hh = mm % 60, str(mm // 60)
        ss, mm = map(lambda x: str(x).rjust(2, "0"), (ss, mm))
        dd = self.days
        if self.microseconds:
            ms = f".{self.microseconds}"
        else:
            ms = ""
        if dd:
            days = self.get_days()
            return f"{days}, {hh}:{mm}:{ss}{ms}"
        return f"{hh}:{mm}:{ss}{mm}"

    def get_days(self):
        """
        получить количество дней в формате 'n дней/дня/день'
        """
        dd = self.days
        ldd = dd % 10
        if (ldd == 0 or 5 <= ldd <= 9) or dd % 100 in {11, 12, 13, 14}:
            day = "дней"
        elif 2 <= ldd <= 4:
            day = "дня"
        else:
            day = "день"
        return f"{dd} {day}"
