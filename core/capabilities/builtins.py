import subprocess
import webbrowser

from .registry import Capability, registry


def open_website(url: str) -> str:
    webbrowser.open(url)
    return f"Opening {url}."


def open_notepad() -> str:
    subprocess.Popen(["notepad.exe"])
    return "Opening Notepad."


registry.register(
    Capability(
        name="open_website",
        description="Open a website in the default browser.",
        handler=open_website,
        requires_confirmation=False,
    )
)

registry.register(
    Capability(
        name="open_notepad",
        description="Open Windows Notepad.",
        handler=open_notepad,
        requires_confirmation=False,
    )
)
