from datetime import datetime


def create_session(session_id, project_name, start_note, tags: str):
    tags_list = tags.split(",") if tags else []

    return {
        "session_id": session_id,
        "project": project_name,
        "start_time": datetime.now().isoformat(),
        "end_time": None,
        "duration": None,
        "note": {"start_note": start_note, "end_note": ""},
        "tags": tags_list,
    }
