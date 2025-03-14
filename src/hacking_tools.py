import hashlib
import os

def crack_md5(hash, wordlist_file):
    with open(wordlist_file, "r") as f:
        for word in f:
            word = word.strip()
            if hashlib.md5(word.encode()).hexdigest() == hash:
                return word
    return None

def find_hidden_file():
    for file in os.listdir("."):
        if file.startswith("."):
            with open(file, "r") as f:
                return f.read().strip()
    return None