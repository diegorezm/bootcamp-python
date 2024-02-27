import pandas as pd
df = pd.read_csv("./data/french_words.csv")

english_wordlist = df['English']
french_wordlist = df['French']

data = {french: english for french, english in zip(french_wordlist,english_wordlist)}

def save(idx: list[int]):
    with open('progress.txt', 'w') as file:
        file.write(' '.join(map(str,idx)))

def get_indexes() -> list[int]:
    try:
        with open('progress.txt', 'r') as file:
         idxs = file.readline()
        return list(map(int, idxs.split()))
    except FileNotFoundError:
        return []
