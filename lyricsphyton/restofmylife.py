import time
import sys

def typewriter_effect(text, total_time=1.7):
    delay = total_time / len(text)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print("")

def sing_song():
    lyrics = [
        "I'll love you for worse or for better",
        "whenever, wherever",
        "for now and forever",
        "the moment I met you",
        "I knew from the start",
        "your heart fit into mine...",
        "I LOVE YOU in Capital letters",
        "whatever the weather",
        "you hold me together",
        "i told you we get here",
        "i knew from the start",
        "my heart got one thing right....",
        "You look like the rest of my life"
    ]
    for line in lyrics:
        typewriter_effect(line, total_time=1.7)
        time.sleep(0.8)

if __name__ == "__main__":
    sing_song()
