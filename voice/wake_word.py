 
import atexit
import pyaudio
import numpy as np
from openwakeword.model import Model

# Configuration
RATE = 16000
CHUNK = 1280
THRESHOLD = 0.5

# Load model only once
print("JARVIS: Loading wake word model...")

model = Model(
    wakeword_models=["hey_jarvis"],
    inference_framework="onnx"
)

audio = pyaudio.PyAudio()
stream = None


def close_microphone():
    global stream

    if stream is not None:
        try:
            stream.stop_stream()
            stream.close()
        except Exception:
            pass

        stream = None


def cleanup():
    close_microphone()
    audio.terminate()
    print("JARVIS: Audio system released.")


def wait_for_wake_word():
    global stream

    try:
        # Open microphone for wake word detection
        if stream is None:
            stream = audio.open(
                format=pyaudio.paInt16,
                channels=1,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK
            )

        model.reset()

        print("JARVIS: Waiting for wake word...")

        while True:
            data = stream.read(
                CHUNK,
                exception_on_overflow=False
            )

            audio_data = np.frombuffer(
                data,
                dtype=np.int16
            )

            prediction = model.predict(audio_data)
            score = prediction.get("hey_jarvis", 0)

            if score > THRESHOLD:

                print(
                    f"JARVIS: Wake word detected! "
                    f"Score: {score:.2f}"
                )

                model.reset()

                # Release microphone before listener starts
                close_microphone()

                return True

    except KeyboardInterrupt:
        close_microphone()
        raise

    except Exception as e:
        print("WAKE WORD ERROR:", e)
        close_microphone()
        return False


# Release audio resources when program exits
atexit.register(cleanup)

print("JARVIS: Wake word model ready!")
 