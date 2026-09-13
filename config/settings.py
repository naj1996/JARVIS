from dataclasses import dataclass
import os


@dataclass(frozen=True)
class Settings:
    assistant_name: str = os.getenv("JARVIS_NAME", "JARVIS")
    wake_word: str = os.getenv("JARVIS_WAKE_WORD", "hey jarvis")
    log_level: str = os.getenv("JARVIS_LOG_LEVEL", "INFO")
    require_confirmation: bool = os.getenv("JARVIS_CONFIRM_ACTIONS", "true").lower() == "true"


settings = Settings()
