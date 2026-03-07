from hablog.models import create_session
import dateparser
from dateutil import parser
from datetime import datetime


def parse_time(text):
    dt = dateparser.parse(text)
    if dt:
        return dt

    try:
        return parser.parse(text)
    except Exception:
        return None


def run(dict, project, note, tags, start_time):

    if dict["active_id"] is not None:
        return

    new_id = len(dict["sessions"]) + 1

    if not start_time:
        start_time = datetime.now().isoformat()
    else:
        parsed_time = parse_time(start_time)
        if parsed_time == None:
            start_time = datetime.now().isoformat()
        else:
            start_time = parsed_time.isoformat()

    new_session = create_session(new_id, project, note, tags, start_time)

    dict["sessions"].append(new_session)
    dict["active_id"] = new_id
