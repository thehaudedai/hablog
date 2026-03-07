from hablog.models import create_session


def run(dict, project, note="", tags=""):
    if dict["active_id"] is not None:
        return

    new_id = len(dict["sessions"]) + 1

    new_session = create_session(new_id, project, note, tags)

    dict["sessions"].append(new_session)
    dict["active_id"] = new_id
