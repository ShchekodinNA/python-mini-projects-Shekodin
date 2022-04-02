import pandas
file_df = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {rw[0]: rw[1] for (indx, rw) in file_df.iterrows()}

user_input = input("Type word for creating NATO alphabet sequence: ").upper()

res_list = [nato_dict[lttr] for lttr in user_input]
print(f"Result: {res_list}")
