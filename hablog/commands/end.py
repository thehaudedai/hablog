from datetime import datetime


def run(dict, note=""):
    if dict["active_id"] is None:
        return

    current_session_id = dict["active_id"] - 1

    current_session = dict["sessions"][current_session_id]

    start_time_object = datetime.fromisoformat(current_session["start_time"])
    end_time_object = datetime.now()

    duration = end_time_object - start_time_object
    end_time = end_time_object.isoformat()

    current_session["end_time"] = end_time
    current_session["duration"] = duration.total_seconds()
    current_session["note"]["end_note"] = note

    dict["active_id"] = None
