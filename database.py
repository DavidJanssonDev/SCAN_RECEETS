from models.expense import Expense


class Database:

    def get_years(self) -> list[int]:
        return [2024, 2025, 2026]

    def get_expenses(self, year: int, month: int) -> list[Expense]:
        return []