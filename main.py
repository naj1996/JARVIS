from core.capabilities import builtins  # noqa: F401 - registers built-in capabilities
from core.orchestrator import JarvisOrchestrator


def main() -> None:
    jarvis = JarvisOrchestrator()
    print("JARVIS v0.1 — text mode")
    print("Type 'exit' to quit.")

    while True:
        try:
            text = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nJARVIS: Goodbye.")
            return

        if text.lower() in {"exit", "quit", "goodbye"}:
            print("JARVIS: Goodbye.")
            return

        result = jarvis.handle_text(text)
        print(f"JARVIS: {result.message}")


if __name__ == "__main__":
    main()
