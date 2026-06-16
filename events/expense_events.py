from textual.message import Message


class MonthSelected(Message):
    def __init__(self, year: int, month: int) -> None:
        self.year = year
        self.month = month
        super().__init__()