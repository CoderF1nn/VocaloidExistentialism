import tts_model as tts


def main():
    teto = tts.tts_model("a3b3f0a9c49340bd8fa722d83c81cb08", "s2.1-pro-free")

    while True:
        tts_input = input("Teto says: ")
        teto.convert("output", tts_input, play=True)

if __name__ == "__main__":
    main()
