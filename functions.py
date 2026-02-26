def get_ticket_status(ticket_id: int):
    return {"ticket_id": ticket_id, "status": "Open"}


def schedule_meeting(date: str, time: str, meeting_room: str):
    return {
        "date": date,
        "time": time,
        "meeting_room": meeting_room,
        "status": "Meeting Scheduled"
    }


def get_expense_balance(employee_id: int):
    return {"employee_id": employee_id, "balance": 5000}


def calculate_performance_bonus(employee_id: int, current_year: int):
    return {
        "employee_id": employee_id,
        "year": current_year,
        "bonus": 75000
    }


def report_office_issue(issue_code: int, department: str):
    return {
        "issue_code": issue_code,
        "department": department,
        "status": "Issue Reported"
    }