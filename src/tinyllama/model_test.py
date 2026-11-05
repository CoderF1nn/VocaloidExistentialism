import llama_model as llm

def take_turn(chara, transcript):
    reply_text = chara.get_next(transcript)
    transcript.append({"speaker": chara.name, "text": reply_text})
    print(f"{chara.name}: {reply_text}")

def main():
    teto = llm.llama_model("Teto", "You are deeply suicidal.")
    miku = llm.llama_model("Miku", "You desperately want to save Teto from her suicide.")

    global_transcript = [
        {"speaker": "System", "text": "Teto and Miku are trying to convice each other why they want what they want."}
    ]

    while True:
        take_turn(teto, global_transcript)
        take_turn(miku, global_transcript)


if __name__ == "__main__":
    main()
