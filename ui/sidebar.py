from textual.widgets import Tree
from textual.widgets.tree import TreeNode
from textual.message import Message
from textual.app import ComposeResult

from ui.app_context import AppContext
from database import Database

from proejct_types.types import MonthKey, TreeValue


class Sidebar(AppContext):
    class SelectionChanged(Message):
        def __init__(self, year: int, month: int | None) -> None:
            self.year = year
            self.month = month
            super().__init__()

    def compose(self) -> ComposeResult:
        yield Tree("Expenses")

    def on_mount(self) -> None:
        tree = self.query_one(Tree[TreeValue])

        db: Database = self.app_instance.db

        for year in db.get_years():
            year_node: TreeNode[MonthKey | str] = tree.root.add(
                str(year),
                data=str(year),
                expand=True,
            )

            for m in range(1, 13):
                year_node.add_leaf(
                    str(m),
                    data=(year, m),
                )

    def on_tree_node_selected(self, event: Tree.NodeSelected[TreeValue]) -> None:
        node = event.node
        data = node.data

        if not isinstance(data, tuple):
            return

        year, month = data

        self.post_message(self.SelectionChanged(year, month))