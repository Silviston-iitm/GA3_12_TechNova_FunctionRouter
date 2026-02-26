import re
import json


def parse_query(q: str):
    q = q.strip()

    # 1. Ticket Status
    match = re.search(r"ticket (\d+)", q, re.IGNORECASE)
    if "status" in q.lower() and match:
        return {
            "name": "get_ticket_status",
            "arguments": json.dumps({
                "ticket_id": int(match.group(1))
            })
        }

    # 2. Schedule Meeting
    match = re.search(
        r"on (\d{4}-\d{2}-\d{2}) at (\d{2}:\d{2}) in (.+)",
        q,
        re.IGNORECASE
    )
    if "schedule" in q.lower() and match:
        return {
            "name": "schedule_meeting",
            "arguments": json.dumps({
                "date": match.group(1),
                "time": match.group(2),
                "meeting_room": match.group(3)
            })
        }

    # 3. Expense Balance
    match = re.search(r"employee (\d+)", q, re.IGNORECASE)
    if "expense" in q.lower() and match:
        return {
            "name": "get_expense_balance",
            "arguments": json.dumps({
                "employee_id": int(match.group(1))
            })
        }

    # 4. Performance Bonus
    match = re.search(r"employee (\d+).*?(\d{4})", q, re.IGNORECASE)
    if "bonus" in q.lower() and match:
        return {
            "name": "calculate_performance_bonus",
            "arguments": json.dumps({
                "employee_id": int(match.group(1)),
                "current_year": int(match.group(2))
            })
        }

    # 5. Office Issue
    match = re.search(r"issue (\d+).*?department", q, re.IGNORECASE)
    dept_match = re.search(r"for the (.+?) department", q, re.IGNORECASE)
    if match and dept_match:
        return {
            "name": "report_office_issue",
            "arguments": json.dumps({
                "issue_code": int(match.group(1)),
                "department": dept_match.group(1)
            })
        }

    return {"error": "Query not recognized"}