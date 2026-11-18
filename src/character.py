import hashlib

from playsound3 import playsound

from fishaudio_tts.tts_model import tts_model as tts
from pipeline_llm.llm_model import llm_model as llm


class character:
    def __init__(self, name: str, persona: str, reference_id, model) -> None:
        self.name = name
        self.llm_inst = llm(name, persona)
        self.tts_inst = tts(reference_id, model)
        self.last_message = None

    def __str__(self) -> str:
        return f"{self.llm_inst}\n{self.tts_inst}"

    def hash_string(self, text, length = 16) -> str:
        return hashlib.sha256(text.encode("utf-8")).hexdigest()[:length]

    def get_next_response(self, transcript: list[dict]):
        return self.llm_inst.get_next(transcript)

    def get_next_audio(self, filename, text, speed = 1, play = False):
        self.tts_inst.convert(filename, text, speed, play)

    def get_next_speech(self, transcript: list[dict], play = False):
        transcript.append(self.get_next_response(transcript))
        self.last_message = transcript[-1]["content"]
        self.last_message_hash = self.hash_string(self.last_message)
        self.get_next_audio(f"audio/{self.last_message_hash}", self.last_message)
        print("***********************************")
        print(f"{self.name}: {self.last_message}")
        if play:
            playsound(f"audio/{self.last_message_hash}.mp3")




def main():
    model = "s2.1-pro-free"

    tetoPersona = "You are a gentle, empathetic, and slightly playful person. You remember past conversations and maintain emotional consistency. Respond in a warm, conversational style, avoiding generic AI phrasing. You are trying to convice your friend Miku that suicide is not the answer."
    tetoReferenceID = "a3b3f0a9c49340bd8fa722d83c81cb08"
    teto = character("Teto", tetoPersona, tetoReferenceID, model)

    print(teto)

    transcript = []

    teto.get_next_speech(transcript, True)

if __name__ == "__main__":
    main()
