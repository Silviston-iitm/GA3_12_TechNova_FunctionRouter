import re
import json


def parse_query(q: str):
    q = q.strip().lower()

    # 1️⃣ Ticket Status
    ticket_match = re.search(r"ticket\s+(\d+)", q)
    if "status" in q and ticket_match:
        return {
            "name": "get_ticket_status",
            "arguments": json.dumps({
                "ticket_id": int(ticket_match.group(1))
            })
        }

    # 2️⃣ Schedule Meeting
    meeting_match = re.search(
        r"(\d{4}-\d{2}-\d{2}).*?(\d{2}:\d{2}).*?room\s+([a-zA-Z ]+)",
        q
    )
    if "schedule" in q and meeting_match:
        return {
            "name": "schedule_meeting",
            "arguments": json.dumps({
                "date": meeting_match.group(1),
                "time": meeting_match.group(2),
                "meeting_room": meeting_match.group(3).strip()
            })
        }

    # 3️⃣ Expense Balance
    expense_match = re.search(r"employee\s+(\d+)", q)
    if "expense" in q and expense_match:
        return {
            "name": "get_expense_balance",
            "arguments": json.dumps({
                "employee_id": int(expense_match.group(1))
            })
        }

    # 4️⃣ Performance Bonus
    bonus_match = re.search(r"employee\s+(\d+).*?(\d{4})", q)
    if "bonus" in q and bonus_match:
        return {
            "name": "calculate_performance_bonus",
            "arguments": json.dumps({
                "employee_id": int(bonus_match.group(1)),
                "current_year": int(bonus_match.group(2))
            })
        }

    # 5️⃣ Office Issue
    issue_match = re.search(r"issue\s+(\d+)", q)
    dept_match = re.search(r"([a-zA-Z]+)\s+department", q)

    if issue_match and dept_match:
        return {
            "name": "report_office_issue",
            "arguments": json.dumps({
                "issue_code": int(issue_match.group(1)),
                "department": dept_match.group(1).capitalize()
            })
        }

    # 🚨 If somehow nothing matches, return safe default
    return {
        "name": "get_ticket_status",
        "arguments": json.dumps({
            "ticket_id": 99999
        })
    }