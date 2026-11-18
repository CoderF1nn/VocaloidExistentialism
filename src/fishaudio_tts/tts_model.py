import logging
import os
from pathlib import Path
import traceback

from dotenv import load_dotenv
from fishaudio.utils import save
from playsound3 import playsound

from fishaudio import FishAudio

load_dotenv()

class tts_model:
    API_KEY = os.getenv("FISH_API_KEY")
    def __init__(self, reference_id, model):
        self.reference_id = reference_id
        self.model = model
        self.client = FishAudio(api_key = self.API_KEY)
        self.last = None

    def __str__(self):
        return f"Model: {self.model}"

    def convert(self, filename, text, speed = 1, play = False):
        filename = f"{filename}.mp3"
        path = Path(filename)
        path.parent.mkdir(parents=True, exist_ok=True)
        try:
            audio = self.client.tts.convert(
                    text=text,
                    reference_id=self.reference_id,
                    speed=speed,
                    model=self.model)
            save(audio, filename)
            if play:
                playsound(filename)
        except Exception:  # noqa: BLE001
            logging.error(traceback.format_exc())  # noqa: LOG015
