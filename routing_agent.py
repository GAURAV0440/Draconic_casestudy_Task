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

class RoutingResult(BaseModel):
    ticket_id: str
    team: Literal["support", "dev", "security", "account", "product", "escalation"]

def route_ticket(ticket: Ticket) -> RoutingResult:
    subject = ticket.subject.lower()
    message = ticket.message.lower()

    # Rule-based routing logic
    if "security" in subject or "vulnerability" in message:
        team = "security"
    elif "api" in subject or "error" in message or "bug" in message:
        team = "dev"
    elif "billing" in subject or "invoice" in message:
        team = "account"
    elif "feature" in subject or "request" in message:
        team = "product"
    elif ticket.customer_tier == "enterprise" and ticket.previous_tickets > 15:
        team = "escalation"
    else:
        team = "support"

    return RoutingResult(ticket_id=ticket.ticket_id, team=team)
