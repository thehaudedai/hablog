def create_session(session_id, project_name, start_note, tags, start_time):
    tags_list = tags.split(",") if tags else []

    return {
        "session_id": session_id,
        "project": project_name,
        "start_time": start_time,
        "end_time": None,
        "duration": None,
        "note": {"start_note": start_note, "end_note": ""},
        "tags": tags_list,
    }


def create_project(name, target, status, tags):
    pass


def create_next_steps(time, note: str, type: str):
    # time is the current time
    # note refers to whatever the user types
    # type: [note / task / blocker / idea]

    # Task: Whatever You Wanna Do Next or Are Doing Now
    # Note: General reminder or context
    # Idea: Quick thoughts or ideas that came up
    # Blocker: Something preventing progress

    pass
