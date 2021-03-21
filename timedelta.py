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
            ldd = dd % 10
            if (ldd == 0 or 5 <= ldd <= 9) or dd % 100 in {11, 12, 13, 14}:
                back = "ей"
            elif 2 <= ldd <= 4:
                back = "я"
            else:
                back = "нь"
            return f"{dd} дн{back}, {hh}:{mm}:{ss}{ms}"
        return f"{hh}:{mm}:{ss}{mm}"
