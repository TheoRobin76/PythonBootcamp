import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}
word = input("Please enter a word: ").upper()

nato = True
while nato:
    try:
        nato_list = [nato_dict[letter] for letter in word]
    except KeyError:
        print("Only enter letters in the alphabet, please")
        word = input("Please enter a word: ").upper()
    else:
        print(nato_list)
        nato = False
