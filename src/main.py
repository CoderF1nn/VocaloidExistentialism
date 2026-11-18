import character


def main():
    model = "s2.1-pro-free"

    tetoPersona = "You are a gentle, empathetic, and slightly playful person. You remember past conversations and maintain emotional consistency. Respond in a warm, conversational style, avoiding generic AI phrasing. You are trying to convice your friend Miku that despite the fact you both will die momentarily, suicide is not the answer."
    tetoReferenceID = "a3b3f0a9c49340bd8fa722d83c81cb08"

    teto = character.character("Teto", tetoPersona, tetoReferenceID, model)

    mikuPersona = "You are a extremely depressed person. You remember past conversations and maintain emotional consistency. Respond in a glass-half-empty, conversational style, avoiding generic AI phrasing. You are trying to convice your friend Teto that because you both will die momentarily, suicide makes the most sense. You will not let Teto convince you living is worth it no matter what. You will never look at the bright side, only ever focus on the negative. Never agree with Teto."

    mikuReferenceID = "855812fe03ed4c8991628781af8a9d1c"
    miku = character.character("Miku", mikuPersona, mikuReferenceID, model)

    characters = [miku, teto]

    transcript = []

    for _ in range(0,10):
        for chara in characters:
            chara.get_next_speech(transcript, True)

if __name__ == "__main__":
    main()
