from datetime import datetime

from hablog.models import create_session
from hablog.utils.time_parser import parse_time
from hablog.utils.result import Result


def run(dict, project, note, tags, start_time):

    if dict["active_id"] is not None:
        return Result.error(
            f"A Session is currently active. End active session to start a new one",
            data={"active_id": dict["active_id"]},
        )

    new_id = len(dict["sessions"]) + 1

    if not start_time:
        start_time = datetime.now().isoformat()
    else:
        parsed_time = parse_time(start_time)
        if parsed_time == None:
            return Result.error(f"Input Invalid!", data={"start_time": start_time})
        else:
            start_time = parsed_time.isoformat()

    if dict["sessions"]:
        prev_session = dict["sessions"][-1]
        end_time_obj = datetime.fromisoformat(prev_session["end_time"])
        start_time_obj = datetime.fromisoformat(start_time)

        if start_time_obj < end_time_obj:
            return Result.error(
                f"You cannot start a session before the end time of the last session",
                data={
                    "previous_session": prev_session,
                    "new_input": {"project": project, "start_time": start_time},
                },
            )

    new_session = create_session(new_id, project, note, tags, start_time)

    dict["sessions"].append(new_session)
    dict["active_id"] = new_id

    return Result.ok(f"New Session Started for {project}", changed=True)
