from datetime import datetime, date


class DateUtility:
    def __init__(self):
        pass

    @staticmethod
    def date_from_string(date_string: str, date_format: int = 1) -> date:
        """
        :param date_string:
        :param date_format:
            date_format == 1: YYYY-MM-DD
        :return:
        """
        if date_format == 1:
            return datetime.strptime(date_string, "%Y-%m-%d").date()
        else:
            raise RuntimeError(f'Date format not support yet, got {date_format}.')