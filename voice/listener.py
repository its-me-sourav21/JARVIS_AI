
import speech_recognition as sr
import pyaudio
import webrtcvad
import collections
import time

recognizer = sr.Recognizer()

RATE = 16000
FRAME_DURATION = 30
FRAME_SIZE = int(RATE * FRAME_DURATION / 1000)
SILENCE_LIMIT = 1.5
MAX_RECORDING_TIME = 60


def listen():
    audio_interface = pyaudio.PyAudio()
    vad = webrtcvad.Vad(2)

    stream = None

    try:
        stream = audio_interface.open(
            format=pyaudio.paInt16,
            channels=1,
            rate=RATE,
            input=True,
            frames_per_buffer=FRAME_SIZE
        )

        print("JARVIS: Listening...")

        frames = []
        speech_started = False
        silence_frames = 0

        silence_limit_frames = int(
            SILENCE_LIMIT * 1000 / FRAME_DURATION
        )

        start_time = time.time()

        while True:

            data = stream.read(
                FRAME_SIZE,
                exception_on_overflow=False
            )

            is_speech = vad.is_speech(data, RATE)

            if is_speech:
                speech_started = True
                silence_frames = 0
            elif speech_started:
                silence_frames += 1

            if speech_started:
                frames.append(data)

            if speech_started and silence_frames >= silence_limit_frames:
                break

            if time.time() - start_time > MAX_RECORDING_TIME:
                break

        if not frames:
            print("JARVIS: No speech detected.")
            return ""

        raw_audio = b"".join(frames)

        audio_data = sr.AudioData(
            raw_audio,
            RATE,
            2
        )

        print("JARVIS: Processing your voice...")

        command = recognizer.recognize_google(audio_data)

        print("YOU:", command)

        return command.lower()

    except sr.UnknownValueError:
        print("JARVIS: Could not understand.")
        return ""

    except sr.RequestError as e:
        print("SPEECH SERVICE ERROR:", e)
        return ""

    except Exception as e:
        print("MIC ERROR:", e)
        return ""

    finally:
        if stream is not None:
            stream.stop_stream()
            stream.close()

        audio_interface.terminate()