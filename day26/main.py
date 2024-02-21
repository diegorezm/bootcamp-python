import pandas as pd

data = pd.read_csv("./nato_phonetic_alphabet.csv")

letters =  {r.iloc[0]: r.iloc[1] for (_,r) in data.iterrows()} 

name = input("Enter a name: ").upper()
name = [word for word in name]

print({word:letters[word] for word in name})
