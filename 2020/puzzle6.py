with open("Inputs/pinput6.txt") as f:
    alph = "abcdefghijklmnopqrstuvwxyz"
    total = num = 0
    cum = ""
    for line in f:
        if len(line) <= 1:
            for letter in alph:
                if cum.count(letter) == num:
                    total += 1
            cum = ""
            num = 0
        else:
            cum += line
            num += 1
            # total += # len(cum)
            # cum = ""
        # for i in range(len(line)-1):
        #     if line[i] not in cum:
        #         cum += line[i]
    print(total)