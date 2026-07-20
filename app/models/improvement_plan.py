from dataclasses import dataclass
from typing import List


@dataclass
class ImprovementItem:
    priority: int
    category: str
    issue: str
    recommendation: str
    impact: str


@dataclass
class ImprovementPlan:
    overall_score: int
    items: List[ImprovementItem]