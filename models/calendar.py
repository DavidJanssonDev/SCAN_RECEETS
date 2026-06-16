from dataclasses import dataclass

@dataclass(frozen=True)
class MonthKey:
    year: int
    month: int | None  # None = year node