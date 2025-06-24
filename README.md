# Draconic_casestudy_Task

# Draconic Case Study – Customer Support Ticket Analyzer (Option A)

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

---

## Project Structure

DRACONIC_CASESTUDY/
├── agents/ # Contains priority and routing agents
├── evaluation/ # Evaluation logic (accuracy, consistency, etc.)
├── docs/
│ └── ai_chat_history.txt
├── test_cases.py # 5 test tickets (from the PDF)
├── main.py # Runs the whole system and prints results
├── notes.txt # What didn’t work and why
├── requirements.txt # Python libraries used
