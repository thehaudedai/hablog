# Import InBuilt Modules
# -------------------------------------------------------------------------------------------
import typer
import json
import os
from datetime import datetime

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

# ------------------------------------------------------------------------------------
# Loading to Dictionary:
if not os.path.exists(FILE):
    with open(FILE, "w") as file:
        json.dump({"active_id": None, "sessions": []}, file, indent=4)
with open(FILE, "r") as file:
    logs_dict = json.load(file)
# ------------------------------------------------------------------------------------


app = typer.Typer()


@app.command("start")
def start_arg(
    project: str, note: str = "", tags: str = "", start_time: str | None = None
):
    if start_time is None:
        start_time = datetime.now().isoformat()
    start.run(logs_dict, project, note, tags, start_time)
    save_logs()


@app.command("end")
def end_arg(note: str = "", end_time: str | None = None):
    end.run(logs_dict, note, end_time)
    save_logs()


@app.command("restart")
def restart_arg(
    project: str,
    end_note: str = "",
    start_note: str = "",
    tags: str = "",
    end_time: str | None = None,
    start_time: str | None = None,
):
    now = datetime.now().isoformat()
    if start_time is None:
        start_time = now
    if end_time is None:
        end_time = now
    end.run(logs_dict, end_note, end_time)
    start.run(logs_dict, project, start_note, tags, start_time)
    save_logs()


@app.command("edit")
def edit_arg():
    save_logs()


@app.command("status")
def status_arg():
    pass


@app.command("break")
def break_arg():
    save_logs()


@app.command("stats")
def stats_arg():
    pass


@app.command("export")
def export_arg():
    pass


@app.command("view")
def view_arg():
    pass


# ------------------------------------------------------------------------------------
# Writing Dictionary to JSON
def save_logs():
    with open(FILE, "w") as file:
        json.dump(logs_dict, file, indent=4)


# ------------------------------------------------------------------------------------
