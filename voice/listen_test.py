from pathlib import Path

import sounddevice as sd
from scipy.io.wavfile import write
from faster_whisper import WhisperModel


SAMPLE_RATE = 16_000
RECORD_SECONDS = 6
AUDIO_PATH = Path("data/runtime/listen_test.wav")


def main() -> None:
    AUDIO_PATH.parent.mkdir(parents=True, exist_ok=True)

    print(f"Speak now for {RECORD_SECONDS} seconds...")
    audio = sd.rec(
        int(RECORD_SECONDS * SAMPLE_RATE),
        samplerate=SAMPLE_RATE,
        channels=1,
        dtype="int16",
    )
    sd.wait()
    write(str(AUDIO_PATH), SAMPLE_RATE, audio)
    print("Audio captured. Transcribing locally...")

    model = WhisperModel("base.en", device="cpu", compute_type="int8")
    segments, _ = model.transcribe(str(AUDIO_PATH), beam_size=5)
    text = " ".join(segment.text.strip() for segment in segments).strip()

    print(f"You said: {text or '[no speech detected]'}")


if __name__ == "__main__":
    main()
