from fishaudio.utils import  save
from playsound3 import playsound
from fishaudio import FishAudio

FISH_API_KEY = "sk-fish-mIyC9-0ymfApxwGpwNuVy7R6K1F5tvTpbdmQgopRAAM"
# Initialize with your API key
client = FishAudio(api_key = FISH_API_KEY)  # reads FISH_API_KEY

# Generate speech with custom voice
audio = client.tts.convert(
    text="HELLO!!!! my name is tetodayo",
    reference_id="a3b3f0a9c49340bd8fa722d83c81cb08",
    model="s2.1-pro-free",
)
save(audio, "testdayo.mp3")
playsound("testdayo.mp3")
