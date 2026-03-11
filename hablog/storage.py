import json
import os

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


# -------------------------------------------------------------------------------------------
def load_logs():
    if not os.path.exists(FILE):
        with open(FILE, "w") as file:
            json.dump({"active_id": None, "sessions": []}, file, indent=4)

    with open(FILE, "r") as file:
        return json.load(file)


# -------------------------------------------------------------------------------------------


# -------------------------------------------------------------------------------------------
def save_logs(data):
    with open(FILE, "w") as file:
        json.dump(data, file, indent=4)


# -------------------------------------------------------------------------------------------
