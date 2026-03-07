# Import InBuilt Modules
# -------------------------------------------------------------------------------------------
import argparse
import json
import os

# -------------------------------------------------------------------------------------------


# Import Custom Packages
# -------------------------------------------------------------------------------------------
from hablog.commands import start, end

# -------------------------------------------------------------------------------------------


# JSON File Directory
# -------------------------------------------------------------------------------------------
# HOME = os.path.expanduser("~")
# HABLOG_DIR = os.path.join(HOME, ".hablog")
# os.makedirs(HABLOG_DIR, exist_ok=True)

# FILE = os.path.join(HABLOG_DIR, "logs.json")

# For Testing:
FILE = "logs.json"
# -------------------------------------------------------------------------------------------


# Variables
# -------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------


# Argument Parsing
# -------------------------------------------------------------------------------------------
def run_app():
    note_var = ""
    tags_var = ""

    # Loading to Dictionary:
    if not os.path.exists(FILE):
        with open(FILE, "w") as file:
            json.dump({"active_id": None, "sessions": []}, file, indent=4)
    with open(FILE, "r") as file:
        logs_dict = json.load(file)

    # Initializing The Parser
    parser = argparse.ArgumentParser(
        description="Hablog, Easily Log Your Habit and Tasks"
    )
    subparser = parser.add_subparsers(
        dest="command", required=True, help="sub-command to run"
    )

    # Start Parser
    start_parser = subparser.add_parser("start", help="Start tracking")
    start_parser.add_argument("project", type=str, help="Name of your project or task")
    start_parser.add_argument(
        "--note", type=str, help="Additional Note when starting your project/task"
    )
    start_parser.add_argument(
        "--tags", type=str, help="Tags to organize your project separated by comma ',' "
    )

    # End Parser
    end_parser = subparser.add_parser("end", help="End tracking")
    end_parser.add_argument(
        "--note", type=str, help="Additional Note when ending your project/task"
    )

    # Status Parser
    status_parser = subparser.add_parser("status", help="Start tracking your task")

    # Restart Parser
    restart_parser = subparser.add_parser("restart", help="Restart tracking your task")
    restart_parser.add_argument(
        "project", type=str, help="Name of your project or task"
    )
    restart_parser.add_argument(
        "--end_note",
        type=str,
        help="Additional Note when ending your current project/task",
    )
    restart_parser.add_argument(
        "--start_note",
        type=str,
        help="Additional note when starting a new project/task",
    )
    restart_parser.add_argument(
        "--tags", type=str, help="Tags to organize your project separated by comma ',' "
    )

    args = parser.parse_args()

    # Argument Condition Checking
    match args.command:

        case "start":
            if args.note:
                note_var = args.note
            if args.tags:
                tags_var = args.tags
            start.run(logs_dict, args.project, note_var, tags_var)

        case "end":
            if args.note:
                note_var = args.note
            end.run(logs_dict, note_var)

        case "restart":
            if args.end_note:
                note_var = args.end_note
            end.run(logs_dict, note_var)
            if args.tags:
                tags_var = args.tags
            if args.start_note:
                start.run(logs_dict, args.project, args.start_note, tags_var)
            else:
                start.run(logs_dict, args.project, "", tags_var)

        # case "status":
        #     pass
        # case "start":
        #     pass

    with open(FILE, "w") as file:
        json.dump(logs_dict, file, indent=4)
