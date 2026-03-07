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
