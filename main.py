import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
while True:
    switcher = 0
    letter = input("Word: ").upper()
    for let in letter:
        status = data[data.letter == let]
        res_status = status.letter.tolist()
        if res_status == []:
            print("Use letters only.")
            switcher = 1
            break
        else:
            pass

    if switcher == 0:
        phoenetic_res = [(data[data.letter == let]).code.item() for let in letter]
        print(phoenetic_res)