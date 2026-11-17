import logging
import os
import traceback

from dotenv import load_dotenv
from fishaudio.utils import save
from playsound3 import playsound

from fishaudio import FishAudio

load_dotenv()

class model:
    API_KEY = os.getenv("FISH_API_KEY")
    def __init__(self, name, reference_id, model):
        self.name = name
        self.reference_id = reference_id
        self.model = model
        self.client = FishAudio(api_key = self.API_KEY)
        self.last = None

    def __str__(self):
        return self.name

    def convert(self, filename, text, speed = 1, play = False):
        filename = f"{filename}.mp3"
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
