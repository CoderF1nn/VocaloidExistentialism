from fishaudio.utils import  save
from playsound3 import playsound
from fishaudio import FishAudio

class model:
    API_KEY = "a3b3f0a9c49340bd8fa722d83c81cb08"
    def __init__(self, name, reference_id, model):
        self.name = name
        self.reference_id = reference_id
        self.model = model
        self.client = FishAudio(api_key = self.API_KEY)
        self.last = None

    def __str__(self):
        return self.name

    def save_convert(self, filename, text, speed = 1):
        try:
            save(self.client.tts.convert(text=text, reference_id=self.reference_id, speed=speed, model=self.model), filename)
        except:
