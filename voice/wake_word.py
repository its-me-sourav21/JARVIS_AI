import time
import pyaudio
import numpy as np
from openwakeword.model import Model


def wait_for_wake_word():

    model = Model(
        wakeword_models=["hey_jarvis"],
        inference_framework="onnx"
    )

    audio = pyaudio.PyAudio()

    stream = audio.open(
        format=pyaudio.paInt16,
        channels=1,
        rate=16000,
        input=True,
        frames_per_buffer=1280
    )

    print("JARVIS: Waiting for wake word...")
    time.sleep(2)  # Initial noise ignore

    try:
        while True:
            data = stream.read(
                1280,
                exception_on_overflow=False
            )

            audio_data = np.frombuffer(data, dtype=np.int16)
            prediction = model.predict(audio_data)

            score = prediction.get("hey_jarvis", 0)

            if score > 0.8:
                print("JARVIS: Wake word detected!")
                return True

    finally:
        stream.stop_stream()
        stream.close()
        audio.terminate()