import transformers
from transformers import pipeline
import torch

transformers.logging.set_verbosity_error()

class llama_model:
    PIPE = pipeline(
        "text-generation",
        model="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
        device=1,
        torch_dtype=torch.bfloat16,
    )

    #Initial statement
    conversation = ["System['Miku is trying to convince Teto to not jump.']"]

    def __init__(self, name: str, persona: str):
        self.name = name
        self.persona = persona


    def format_transcript(self, transcript: list[dict]) -> list[dict]:
        formatted_messages = [
            {
                "role": "system",
                "content": f"You are roleplaying as {self.name}. {self.persona}\nStay strictly in character and keep responses concise."
            }
        ]

        for entry in transcript:
            speaker = entry["speaker"]
            text = entry["text"]

            if speaker == self.name:
                formatted_messages.append({"role": "assistant", "content": text})
            else:
                formatted_messages.append({"role": "user", "content": f"[{speaker}]: {text}"})

        return formatted_messages

    def get_next(self, transcript: list[dict]) -> str:
        formatted_messages = self.format_transcript(transcript)

        out = llama_model.PIPE(
            formatted_messages,
            max_new_tokens=60,
            do_sample=True,
            temperature=0.7,
            repetition_penalty=1.2,
        )

        new_message = out[0]["generated_text"][-1]["content"]

        return new_message.strip()
