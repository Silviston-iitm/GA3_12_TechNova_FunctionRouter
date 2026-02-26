import re
import json


def parse_query(q: str):
    q = q.strip()

    # 1️⃣ Ticket Status
    match = re.search(r"What is the status of ticket (\d+)\?", q)
    if match:
        return {
            "name": "get_ticket_status",
            "arguments": json.dumps({
                "ticket_id": int(match.group(1))
            })
        }

    # 2️⃣ Schedule Meeting
    match = re.search(
        r"Schedule a meeting on (\d{4}-\d{2}-\d{2}) at (\d{2}:\d{2}) in (.+)\.",
        q
    )
    if match:
        return {
            "name": "schedule_meeting",
            "arguments": json.dumps({
                "date": match.group(1),
                "time": match.group(2),
                "meeting_room": match.group(3)
            })
        }

    # 3️⃣ Expense Balance
    match = re.search(r"Show my expense balance for employee (\d+)\.", q)
    if match:
        return {
            "name": "get_expense_balance",
            "arguments": json.dumps({
                "employee_id": int(match.group(1))
            })
        }

    # 4️⃣ Performance Bonus
    match = re.search(
        r"Calculate performance bonus for employee (\d+) for (\d{4})\.",
        q
    )
    if match:
        return {
            "name": "calculate_performance_bonus",
            "arguments": json.dumps({
                "employee_id": int(match.group(1)),
                "current_year": int(match.group(2))
            })
        }

    # 5️⃣ Office Issue
    match = re.search(
        r"Report office issue (\d+) for the ([A-Za-z]+) department\.",
        q
    )
    if match:
        return {
            "name": "report_office_issue",
            "arguments": json.dumps({
                "issue_code": int(match.group(1)),
                "department": match.group(2)
            })
        }

    # Should never happen
    return {
        "name": "get_ticket_status",
        "arguments": json.dumps({
            "ticket_id": 0
        })
    }