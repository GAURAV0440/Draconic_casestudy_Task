from pydantic import BaseModel
from typing import Literal

class Ticket(BaseModel):
    ticket_id: str
    customer_tier: Literal["free", "premium", "enterprise"]
    subject: str
    message: str
    previous_tickets: int
    monthly_revenue: float
    account_age_days: int

class PriorityResult(BaseModel):
    ticket_id: str
    priority: Literal["low", "medium", "high", "critical"]

def analyze_priority(ticket: Ticket) -> PriorityResult:
    # Heuristics-based scoring
    score = 0

    if ticket.customer_tier == "enterprise":
        score += 3
    elif ticket.customer_tier == "premium":
        score += 2

    if ticket.monthly_revenue > 10000:
        score += 3
    elif ticket.monthly_revenue > 5000:
        score += 2
    elif ticket.monthly_revenue > 1000:
        score += 1

    if ticket.previous_tickets > 10:
        score += 2
    elif ticket.previous_tickets > 5:
        score += 1

    if "urgent" in ticket.subject.lower() or "security" in ticket.subject.lower():
        score += 3
    elif "error" in ticket.subject.lower() or "fail" in ticket.subject.lower():
        score += 2

    # Basic rule-based mapping
    if score >= 8:
        priority = "critical"
    elif score >= 5:
        priority = "high"
    elif score >= 3:
        priority = "medium"
    else:
        priority = "low"

    return PriorityResult(ticket_id=ticket.ticket_id, priority=priority)
