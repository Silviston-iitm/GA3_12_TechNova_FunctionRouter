import re
import json


def parse_query(q: str):
    q = q.strip()

    # Normalize spaces
    q = re.sub(r"\s+", " ", q)

    # 1️⃣ Ticket Status
    ticket = re.search(r"ticket (\d+)", q, re.IGNORECASE)
    if ticket and "status" in q.lower():
        return {
            "name": "get_ticket_status",
            "arguments": json.dumps({
                "ticket_id": int(ticket.group(1))
            })
        }

    # 2️⃣ Schedule Meeting
    meeting = re.search(
        r"(\d{4}-\d{2}-\d{2}).*?(\d{2}:\d{2}).*?room ([A-Za-z ]+)",
        q,
        re.IGNORECASE
    )
    if meeting and "schedule" in q.lower():
        return {
            "name": "schedule_meeting",
            "arguments": json.dumps({
                "date": meeting.group(1),
                "time": meeting.group(2),
                "meeting_room": meeting.group(3).strip()
            })
        }

    # 3️⃣ Expense Balance
    emp = re.search(r"employee (\d+)", q, re.IGNORECASE)
    if emp and "expense" in q.lower():
        return {
            "name": "get_expense_balance",
            "arguments": json.dumps({
                "employee_id": int(emp.group(1))
            })
        }

    # 4️⃣ Performance Bonus
    bonus = re.search(r"employee (\d+).*?(\d{4})", q, re.IGNORECASE)
    if bonus and "bonus" in q.lower():
        return {
            "name": "calculate_performance_bonus",
            "arguments": json.dumps({
                "employee_id": int(bonus.group(1)),
                "current_year": int(bonus.group(2))
            })
        }

    # 5️⃣ Office Issue
    issue = re.search(r"issue (\d+)", q, re.IGNORECASE)
    dept = re.search(r"for the ([A-Za-z]+) department", q, re.IGNORECASE)

    if issue and dept:
        return {
            "name": "report_office_issue",
            "arguments": json.dumps({
                "issue_code": int(issue.group(1)),
                "department": dept.group(1)
            })
        }

    # Absolute fallback
    return {
        "name": "get_ticket_status",
        "arguments": json.dumps({
            "ticket_id": 1
        })
    }