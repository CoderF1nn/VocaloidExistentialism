import transformers
from transformers import pipeline

transformers.logging.set_verbosity_error()

class llm_model:
    PIPE = pipeline(
        "text-generation",
        model="Qwen/Qwen2.5-1.5B-Instruct",
        device=1,
        trust_remote_code=True
    )

    def __init__(self, name: str, persona: str):
        self.name = name
        self.persona = persona
        self.formatted_messages = [
            {
                "role": "system",
                "content": f"You are named {self.name}. {self.persona} Stay strictly in character and keep responses concise, direct, and short."
            }
        ]

    def __str__(self):
        return f"Name: {self.name}\nPersona: {self.persona}"

    def transcript_app_last(self, transcript: list[dict]):
        #appends to current transcript last input
        if len(transcript) != 0 and transcript[-1]["role"] == "assistant":
            self.formatted_messages.append({"role": "user", "content": transcript[-1]["content"]})

    def fix_sentance(self, message):
          parsed = message["content"].strip()
          punctuation = [parsed.rfind("."), parsed.rfind("?"), parsed.rfind("!")]
          last_punct_idx = max(punctuation)

          if parsed[last_punct_idx] != parsed[-1]:
            #print("FOUND LAST ISSUE")
            return parsed[: last_punct_idx + 1].strip()

          return parsed

    def get_next(self, transcript: list[dict]):
        self.transcript_app_last(transcript)

        out = llm_model.PIPE(
            self.formatted_messages,
            max_new_tokens=60,
            do_sample=True,
            temperature=0.7,
            repetition_penalty=1.2,
        )

        self.new_message = out[0]["generated_text"][-1]
        self.new_message["content"] = self.fix_sentance(self.new_message)
        self.formatted_messages.append(self.new_message)


        return self.new_message
