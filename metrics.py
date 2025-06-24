from typing import List, Dict
from collections import Counter
from agents.priority_agent import PriorityResult
from agents.routing_agent import RoutingResult

def evaluate_accuracy(predictions: List[str], expected: List[str]) -> float:
    correct = sum(p == e for p, e in zip(predictions, expected))
    return round((correct / len(expected)) * 100, 2)

def evaluate_priority_distribution(results: List[PriorityResult]) -> Dict[str, int]:
    return dict(Counter(r.priority for r in results))

def evaluate_routing_distribution(results: List[RoutingResult]) -> Dict[str, int]:
    return dict(Counter(r.team for r in results))

def evaluate_consistency(results: List[PriorityResult], tickets: List[Dict]) -> float:
    mismatches = 0
    for r, t in zip(results, tickets):
        if t['customer_tier'] == 'enterprise' and r.priority in ['low', 'medium']:
            mismatches += 1
    return round(100 - (mismatches / len(results) * 100), 2)
