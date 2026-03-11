from typing import Optional, List, Dict

from rich.panel import Panel
from rich.console import Console
from rich.pretty import Pretty

console = Console()


class Result:

    # ---------------------------------------------------------------------------------------------
    def __init__(
        self,
        status: str,
        message: str,
        changed: bool = False,
        warnings: Optional[List[str]] = None,
        exception: str | None = None,
        data: Optional[Dict] = None,
    ):
        self.status = status
        self.message = message
        self.changed = changed
        self.warnings = warnings or []
        self.exception = exception
        self.data = data

    # ---------------------------------------------------------------------------------------------
    @classmethod
    def ok(
        cls,
        message: str,
        changed: bool = False,
        data: Optional[Dict] = None,
        warnings: Optional[List[str]] = None,
    ):
        return cls("ok", message=message, changed=changed, data=data, warnings=warnings)

    # ---------------------------------------------------------------------------------------------

    # ---------------------------------------------------------------------------------------------
    @classmethod
    def info(
        cls,
        message: str,
        changed: bool = False,
        data: Optional[Dict] = None,
        warnings: Optional[List[str]] = None,
    ):
        return cls(
            "info", message=message, changed=changed, data=data, warnings=warnings
        )

    # ---------------------------------------------------------------------------------------------

    # ---------------------------------------------------------------------------------------------
    @classmethod
    def error(
        cls, message: str, data: Optional[Dict] = None, exception: Optional[str] = None
    ):
        return cls(
            "error", message=message, data=data, changed=False, exception=exception
        )

    # ---------------------------------------------------------------------------------------------

    # ---------------------------------------------------------------------------------------------
    def display(self, save_func, show_exception: bool = True):
        if self.status == "error":
            console.print(Panel(self.message, title="🛑 Error", expand=True))
            if show_exception and self.exception:
                # Show Exception
                pass
        elif self.status == "ok":
            console.print(Panel(self.message, title="✅ Success", expand=True))

        elif self.status == "info":
            console.print(Panel(self.message, title="ℹ️ Info", expand=True))

        for warning in self.warnings:
            console.print(Panel(warning, title="⚠️ Warning", expand=True))

        if self.data:
            special_printed = False

            if "previous_session" in self.data:
                console.print(
                    Panel(
                        Pretty(self.data["previous_session"], expand_all=True),
                        title="📊 Data | Previous Session",
                        expand=True,
                    )
                )
                special_printed = True
            if "new_input" in self.data:
                console.print(
                    Panel(
                        Pretty(
                            self.data["new_input"],
                            expand_all=False,
                        ),
                        title="📊 Data | New Input",
                        expand=True,
                    )
                )
                special_printed = True

            if not special_printed:
                console.print(
                    Panel(
                        Pretty(self.data, expand_all=False),
                        title="📊 Data",
                        expand=True,
                    )
                )

        if self.changed:
            save_func()

    # ---------------------------------------------------------------------------------------------
