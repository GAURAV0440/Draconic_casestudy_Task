# Draconic_casestudy_Task

Customer Support Ticket Analyzer (Option A)

Hi! This is my submission for the Draconic AI/ML Engineer Case Study.  
I chose **Option A** – building a support ticket analyzer using multiple AI agents.

---

## What This Project Does

This project reads support tickets and uses two specialized agents to:

1. **Decide Priority** – How urgent is the ticket?  
2. **Route Ticket** – Which team should handle it? (support, dev, security, etc.)

The system also runs evaluation checks to measure how well the agents are performing.

---

## Tech Used

- Python 3.10  
- [Pydantic](https://docs.pydantic.dev/) for modeling ticket data  
- Rule-based agents (no external APIs)  
- Command-line based testing and evaluation
