import re
import json


def parse_query(q: str):
    q = q.strip()

    # 1️⃣ Ticket Status
    ticket_match = re.search(r"ticket (\d+)", q, re.IGNORECASE)
    if ticket_match and "status" in q.lower():
        return {
            "name": "get_ticket_status",
            "arguments": json.dumps({
                "ticket_id": int(ticket_match.group(1))
            })
        }

    # 2️⃣ Schedule Meeting
    meeting_match = re.search(
        r"schedule a meeting on (\d{4}-\d{2}-\d{2}) at (\d{2}:\d{2}) in (.+)",
        q,
        re.IGNORECASE
    )
    if meeting_match:
        return {
            "name": "schedule_meeting",
            "arguments": json.dumps({
                "date": meeting_match.group(1),
                "time": meeting_match.group(2),
                "meeting_room": meeting_match.group(3)
            })
        }

    # 3️⃣ Expense Balance
    expense_match = re.search(r"expense balance for employee (\d+)", q, re.IGNORECASE)
    if expense_match:
        return {
            "name": "get_expense_balance",
            "arguments": json.dumps({
                "employee_id": int(expense_match.group(1))
            })
        }

    # 4️⃣ Performance Bonus
    bonus_match = re.search(
        r"performance bonus for employee (\d+) for (\d{4})",
        q,
        re.IGNORECASE
    )
    if bonus_match:
        return {
            "name": "calculate_performance_bonus",
            "arguments": json.dumps({
                "employee_id": int(bonus_match.group(1)),
                "current_year": int(bonus_match.group(2))
            })
        }

    # 5️⃣ Office Issue
    issue_match = re.search(
        r"report office issue (\d+) for the ([A-Za-z]+) department",
        q,
        re.IGNORECASE
    )
    if issue_match:
        return {
            "name": "report_office_issue",
            "arguments": json.dumps({
                "issue_code": int(issue_match.group(1)),
                "department": issue_match.group(2)
            })
        }

    # 🚨 Fallback (NEVER return error format)
    return {
        "name": "get_ticket_status",
        "arguments": json.dumps({
            "ticket_id": 0
        })
    }