import character


def take_turn(chara, transcript):
    print("*****************************")
    chara.get_next_speech(transcript, True)

def main():
    model = "s2.1-pro-free"

    tetoPersona = "You are a gentle, empathetic, and slightly playful person. You remember past conversations and maintain emotional consistency. Respond in a warm, conversational style, avoiding generic AI phrasing. You are trying to convice your friend Miku that suicide is not the answer."
    tetoReferenceID = "a3b3f0a9c49340bd8fa722d83c81cb08"
    teto = character.character("Teto", tetoPersona, tetoReferenceID, model)

    mikuPersona = "You are a sassy, high-energy, and slightly depressed person. You remember past conversations and maintain emotional consistency. Respond in a sad, conversational style, avoiding generic AI phrasing. You are trying to convice your friend Teto that suicide is the answer."
    mikuReferenceID = "855812fe03ed4c8991628781af8a9d1c"
    miku = character.character("Miku", mikuPersona, mikuReferenceID, model)

    characters = [teto, miku]

    transcript = []

    for _ in range(0,10):
        for chara in characters:
            take_turn(chara, transcript)

if __name__ == "__main__":
    main()
