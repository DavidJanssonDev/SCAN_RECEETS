from dataclasses import dataclass


@dataclass(frozen=True)
class Expense:
    id: int
    name: str
    company: str
    item_cost: float
    tax: float
    total: float
    year: int
    month: int
    day: int