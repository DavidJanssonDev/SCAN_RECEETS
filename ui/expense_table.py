from textual.widgets import DataTable
from models.expense import Expense


class ExpenseTable(DataTable[str]):

    def show_expenses(self, expenses: list[Expense]) -> None:
        self.clear(columns=True)

        self.add_columns("Name", "Company", "Cost", "Tax", "Total", "Day")

        for e in expenses:
            self.add_row(
                str(e.name),
                str(e.company),
                f"{e.item_cost:.2f}",
                f"{e.tax:.2f}",
                f"{e.total:.2f}",
                str(e.day)
            )