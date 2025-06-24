from agents.priority_agent import analyze_priority, Ticket as PriorityTicket
from agents.routing_agent import route_ticket, Ticket as RoutingTicket
from test_cases import test_tickets
from evaluation.metrics import (
    evaluate_accuracy,
    evaluate_priority_distribution,
    evaluate_routing_distribution,
    evaluate_consistency
)
from colorama import Fore, Style

# Ground truth labels (manually assumed for demo)
expected_priorities = ["low", "high", "medium", "high", "critical"]
expected_teams = ["support", "support", "product", "dev", "security"]

priority_outputs = []
routing_outputs = []

print(f"{Fore.CYAN}=== Running Multi-Agent Ticket Analyzer ==={Style.RESET_ALL}\n")

for i, ticket_data in enumerate(test_tickets):
    ticket_id = ticket_data['ticket_id']

    p_ticket = PriorityTicket(**ticket_data)
    r_ticket = RoutingTicket(**ticket_data)

    priority_result = analyze_priority(p_ticket)
    routing_result = route_ticket(r_ticket)

    priority_outputs.append(priority_result)  # Store full object
    routing_outputs.append(routing_result)

    print(f"{Fore.YELLOW}Ticket ID: {ticket_id}{Style.RESET_ALL}")
    print(f"  Priority  → {Fore.RED}{priority_result.priority}{Style.RESET_ALL} | Expected: {expected_priorities[i]}")
    print(f"  Routed To → {Fore.GREEN}{routing_result.team}{Style.RESET_ALL} | Expected: {expected_teams[i]}\n")

# Evaluation
print(f"{Fore.MAGENTA}--- Evaluation Report ---{Style.RESET_ALL}")
print(f"Accuracy (Priority)               → {evaluate_accuracy([p.priority for p in priority_outputs], expected_priorities)}%")
print(f"Accuracy (Routing)                → {evaluate_accuracy([r.team for r in routing_outputs], expected_teams)}%")
print(f"Tier-based Priority Consistency   → {evaluate_consistency(priority_outputs, test_tickets)}%")
print(f"Priority Distribution             → {evaluate_priority_distribution(priority_outputs)}")
print(f"Routing Distribution              → {evaluate_routing_distribution(routing_outputs)}")
