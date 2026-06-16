from textual.app import App

from ui.sidebar import Sidebar
from ui.expense_table import ExpenseTable
from events.expense_events import MonthSelected
from database import Database
from models.expense import Expense


class ExpenseApp(App[None]):
    db: Database

    def __init__(self) -> None:
        super().__init__()
        self.db = Database()

    def compose(self):
        yield Sidebar()
        yield ExpenseTable()

    def on_month_selected(self, event: MonthSelected) -> None:
        expenses: list[Expense] = self.db.get_expenses(
            event.year,
            event.month
        )

        table = self.query_one(ExpenseTable)
        table.show_expenses(expenses)

if __name__ == "__main__":
    ExpenseApp().run()