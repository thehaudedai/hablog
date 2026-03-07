from datetime import datetime, timedelta
import dateparser
from dateutil import parser


def parse_time(text):
    dt = dateparser.parse(text)
    if dt:
        return dt

    try:
        return parser.parse(text)
    except Exception:
        return None


def run(dict, note, end_time):
    if dict["active_id"] is None:
        return

    current_session_id = dict["active_id"] - 1
    current_session = dict["sessions"][current_session_id]

    start_time_object = datetime.fromisoformat(current_session["start_time"])

    if end_time is None:
        end_time_object = datetime.now()
    else:
        parsed = parse_time(end_time)
        if parsed is None:
            end_time_object = datetime.now()
        else:
            end_time_object = parsed

    if end_time_object < start_time_object:
        end_time_object = start_time_object + timedelta(hours=2)
        print("End time given before the start time, using start + 2 hours fallback")

    duration = end_time_object - start_time_object

    current_session["end_time"] = end_time_object.isoformat()
    current_session["duration"] = duration.total_seconds()
    current_session["note"]["end_note"] = note

    dict["active_id"] = None
