import pandas as pd


# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

nato_df = pd.read_csv('nato_phonetic_alphabet.csv')
nato_dict = {row.letter:row.code for index, row in nato_df.iterrows()}
print(nato_dict)


name = input('Enter your name: ').upper()
name_phonetic_list = [nato_dict[item] for item in name ]
print(name_phonetic_list)