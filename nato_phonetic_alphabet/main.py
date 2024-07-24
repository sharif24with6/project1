import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")
words= input("Enter a word : ").upper()

phonetic_dict={row.letter:row.code for (index,row) in data.iterrows()}
result=[phonetic_dict[letter] for letter in words]
print(result)
