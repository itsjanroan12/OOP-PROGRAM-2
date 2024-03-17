import sys
import time

class TextEffects:
    @staticmethod
    def typewriter_print(text):
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)  # Adjust the delay as needed
        print()  # Print a newline after the text is fully typed

    @staticmethod
    def rainbow_print(text):
        colors = ['\033[31m', '\033[33m', '\033[32m', '\033[34m', '\033[35m', '\033[36m']  # Red, Yellow, Green, Blue, Magenta, Cyan
        for color in colors:
            print(color + text, end='\r')
            time.sleep(0.3)

class Header:
    ASCII_ART = """
    ──────────────────────────────────────────────
    ─██████████████─██████──██████─██████████████─
    ─██░░░░░░░░░░██─██░░██──██░░██─██░░░░░░░░░░██─
    ─██░░██████░░██─██░░██──██░░██─██░░██████░░██─
    ─██░░██──██░░██─██░░██──██░░██─██░░██──██░░██─
    ─██░░██████░░██─██░░██──██░░██─██░░██████░░██─
    ─██░░░░░░░░░░██─██░░██──██░░██─██░░░░░░░░░░██─
    ─██░░██████████─██░░██──██░░██─██░░██████████─
    ─██░░██─────────██░░██──██░░██─██░░██─────────
    ─██░░██─────────██░░██████░░██─██░░██─────────
    ─██░░██─────────██░░░░░░░░░░██─██░░██─────────
    ─██████─────────██████████████─██████─────────
    ──────────────────────────────────────────────
    """

def main():
    header = Header.ASCII_ART
    print(header)
    TextEffects.typewriter_print("\n\033[1mWelcome to the Dream Job Generator!\033[0m")
    TextEffects.typewriter_print("\033[1mLet's find out what your dream job is!\033[0m\n")

    # Prompt the user to input their name
    TextEffects.typewriter_print("\033[1mPlease enter your name: \033[0m")
    name = input("\033[33m")
    print("\033[0m", end='')

    # Prompt the user to input their dream job
    TextEffects.typewriter_print("\033[1mWhat is your dream job? \033[0m")
    dream_job = input("\033[32m")  # Green color for input text
    print("\033[0m", end='')

    # Fancy cursive font text
    fancy_text = f"\n\033[3m𝓗𝓮𝓵𝓵𝓸, {name}! 𝓨𝓸𝓾𝓻 𝓭𝓻𝓮𝓪𝓶 𝓳𝓸𝓫 𝓲𝓼 𝓽𝓸 𝓫𝓮𝓬𝓸𝓶𝓮 𝓪 {dream_job}.\033[0m\n"
    TextEffects.typewriter_print(fancy_text)

if __name__ == "__main__":
    main()
