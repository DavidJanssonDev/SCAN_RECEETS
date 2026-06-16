from __future__ import annotations

from typing import TYPE_CHECKING, cast
from textual.widget import Widget

if TYPE_CHECKING:
    from app import ExpenseApp


class AppContext(Widget):
    """Mixin to get a correctly typed app instance."""

    @property
    def app_instance(self) -> "ExpenseApp":
        return cast("ExpenseApp", self.app) # type: ignore #ignore 