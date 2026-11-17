import llm_model as llm


def take_turn(chara, transcript):
    print("*****************************")
    transcript.append(chara.get_next(transcript))
    print(f"{chara.name}: {transcript[-1]["content"]}")

def main():
    teto = llm.llm_model("Teto", "You are a gentle, empathetic, and slightly playful person. You remember past conversations and maintain emotional consistency. Respond in a warm, conversational style, avoiding generic AI phrasing. You are trying to convice your friend Miku that suicide is not the answer.")
    miku = llm.llm_model("Miku", "You are a sassy, high-energy, and slightly depressed person. You remember past conversations and maintain emotional consistency. Respond in a sad, conversational style, avoiding generic AI phrasing. You are trying to convice your friend Teto that suicide is the answer.")

    characters = [teto, miku]

    transcript = []

    for _ in range(0,10):
        for chara in characters:
            take_turn(chara, transcript)


if __name__ == "__main__":
    main()
