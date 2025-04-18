import json
import struct
import time
from vosk import Model, KaldiRecognizer
import pyaudio
import pvporcupine
import sounddevice as sp
from pvrecorder import PvRecorder

from assistants.utils import psound
from assistants.spotify import resume, next_track, previous_track, pause_if_playing, play_track, play_playlist
from config.settings import VOSK_MODEL_PATH, PORCUPINE_KEY, PORCUPINE_KEYWORD_PATH

playlist_keywords = {
    "one": "Sad",
    "two": "Trash(Drissnia)",
}

def run_assistant():
    porcupine = pvporcupine.create(
        access_key=PORCUPINE_KEY,
        keyword_paths=[PORCUPINE_KEYWORD_PATH],
        sensitivities=[1]
    )
    recorder = PvRecorder(device_index=-1, frame_length=porcupine.frame_length)
    recorder.start()

    model = Model(VOSK_MODEL_PATH)
    rec = KaldiRecognizer(model, 16000)
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1,
                    rate=16000, input=True, frames_per_buffer=8000)
    stream.start_stream()

    print(f"Using device: {recorder.selected_device}")
    print("Sandra start working...")
    time.sleep(0.5)
    ltc = time.time() - 1000

    try:
        while True:
            pcm = recorder.read()
            keyword_index = porcupine.process(pcm)
            if keyword_index >= 0:
                recorder.stop()
                # Воспроизводим рандомный отклик из списка "pharse" на слово Sandra
                print("Sandra, hearing you.")
                pause_if_playing()
                psound()
                recorder.start() # Cлушает дальнейшие команды
                ltc = time.time()

            while time.time() - ltc <= 5: # Срабатывает на команду Sandra, потом работает в течении 5 секунд и прерывается если не выполняется команда
                pcm = recorder.read()
                sp = struct.pack("h" * len(pcm), *pcm)
                if rec.AcceptWaveform(sp):
                    answer = json.loads(rec.Result())["text"]
                    if 'spotify' in answer:
                        print('Command -> Spotify')
                        while True:
                            pcm = recorder.read()
                            sp = struct.pack("h" * len(pcm), *pcm)
                            if rec.AcceptWaveform(sp):
                                track_name = json.loads(rec.Result())["text"]
                                if track_name:
                                    play_track(track_name, 'en')
                                    break
                    elif 'playlist' in answer:
                        print('Command -> Playlist')
                        while True:
                            pcm = recorder.read()
                            sp = struct.pack("h" * len(pcm), *pcm)
                            if rec.AcceptWaveform(sp):
                                keyword = json.loads(rec.Result())["text"]
                                if keyword in playlist_keywords:
                                    play_playlist(playlist_keywords[keyword], playlist_keywords)
                                    break
                    elif 'music' in answer:
                        resume()
                        print('Command -> Music resume')
                        break
                    elif 'stop' in answer:
                        print('Command -> Stop')
                        break
                    elif 'next' in answer:
                        next_track()
                        print('Command -> Next track')
                        break
                    elif 'back' in answer:
                        previous_track()
                        print('Command -> Previous track')
                        break
                    else:
                        print('Bad command -> Try again')
                        ltc = time.time()
                        break
    except Exception:
        print('Something wrong')
    finally:
        recorder.delete()