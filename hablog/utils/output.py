from rich.console import Console
from hablog.utils.result import Result
from hablog.storage import save_logs

console = Console()


def handle_output(data, result: Result, show_exception: bool = False):

    if result.status == "error":
        pass
    if result.status == "ok":

        for warning in result.warnings:
            # print Warning:
            pass

    if result.changed:
        save_logs(data)
