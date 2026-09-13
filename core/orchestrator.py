from dataclasses import dataclass

from config.settings import settings
from core.capabilities.registry import registry


@dataclass
class CommandResult:
    ok: bool
    message: str


class JarvisOrchestrator:
    """Central coordinator. Voice, LLM, memory and UI will plug into this layer."""

    def handle_text(self, text: str) -> CommandResult:
        query = text.strip()
        if not query:
            return CommandResult(False, "I didn't receive a command.")

        lowered = query.lower()
        if lowered in {"open notepad", "launch notepad", "start notepad"}:
            message = registry.execute("open_notepad")
            return CommandResult(True, message)

        if lowered.startswith("open ") and "." in lowered:
            target = query[5:].strip()
            url = target if target.startswith(("http://", "https://")) else f"https://{target}"
            message = registry.execute("open_website", url=url)
            return CommandResult(True, message)

        return CommandResult(
            True,
            f"{settings.assistant_name} received: {query}. LLM routing will be connected in the next phase.",
        )
