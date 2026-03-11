from hablog.utils.result import Result
from hablog.utils.time_parser import parse_time
from hablog.commands import start, end

from datetime import datetime


# TODO: If no active, start a new task but send warning that nothing was ended, better to use start if no active task is available.


def run(dict, project, end_note, start_note, tags, end_time, start_time):

    now = datetime.now().isoformat()
    times = [end_time, start_time]

    for time in times:
        if not time:
            time = now
        else:
            parsed = parse_time(time)
            if parsed == None:
                return Result.error(f"{time} is not a valid time input")
            else:
                time = parsed.isoformat()

    if dict["active_id"] is None:
        start.run(dict, project, start_note, tags, start_time)
        return Result.ok(
            f"Started New Session For {project}",
            changed=True,
            warnings=[
                "No Active Session",
                "Use start command to start a new session when there is no active session",
                "Started New Session But Nothing Was Ended",
            ],
        )

    session_id = dict["active_id"]
    end.run(dict, end_note, end_time)

    return Result.ok(
        f"Session Restarted | Session Id: {session_id} Ended | Started New Session For {project}",
        changed=True,
    )
