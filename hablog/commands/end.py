from datetime import datetime, timedelta

from hablog.utils.time_parser import parse_time
from hablog.utils.result import Result


def run(dict, note, end_time):
    if dict["active_id"] is None:
        return Result.info(
            "No Active Session To End",
            changed=False,
            warnings=["End a session only when there is a session active"],
        )

    current_session_id = dict["active_id"] - 1
    current_session = dict["sessions"][current_session_id]

    start_time_object = datetime.fromisoformat(current_session["start_time"])

    if end_time is None:
        end_time_object = datetime.now()
    else:
        parsed = parse_time(end_time)
        if parsed is None:
            return Result.error(f"{end_time} is not a valid time input")
        else:
            end_time_object = parsed

    if end_time_object < start_time_object:
        return Result.error(
            f"End Time cannot be before the start time of a session | End Time: {end_time_object.isoformat()} | Start Time: {start_time_object.isoformat()}"
        )

    duration = end_time_object - start_time_object

    current_session["end_time"] = end_time_object.isoformat()
    current_session["duration"] = duration.total_seconds()
    current_session["note"]["end_note"] = note

    dict["active_id"] = None

    return Result.ok(
        f"Successfully Ended {current_session['project']} Session with Session Id: {current_session_id + 1}",
        changed=True,
    )
