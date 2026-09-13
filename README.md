# JARVIS

A modular, voice-first Windows AI assistant inspired by the JARVIS computer interface.

## Vision

JARVIS is being built as a real desktop agent rather than a simple chatbot:

- Wake-word driven voice interaction
- Natural speech recognition and text-to-speech
- LLM reasoning and planning
- Safe, explicit capability/tool registry
- Windows desktop control
- Browser automation
- Persistent memory and document retrieval
- Cinematic desktop HUD
- Multi-step task execution

## Architecture

```text
Microphone -> Wake Word -> Speech-to-Text -> Orchestrator
                                             |
                         +-------------------+-------------------+
                         |                   |                   |
                       Memory             Planner          Capability Registry
                         |                   |                   |
                         +-------------------+-------------------+
                                             |
                                      Tool Execution
                                             |
                                    Voice / HUD Response
```

## Development phases

1. Core orchestrator and capability registry
2. Voice pipeline
3. LLM provider
4. Windows capabilities
5. Browser capabilities
6. Persistent memory
7. HUD
8. Multi-step agent planning

## Safety principle

The language model chooses from registered capabilities. It does not receive unrestricted operating-system access. Destructive or sensitive capabilities will require explicit confirmation.

## Status

**v0.1 — foundation in progress**
