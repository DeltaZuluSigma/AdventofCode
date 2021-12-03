valid = 0
with open("Inputs/pinput2.txt") as f:
    for line in f:
        idx1 = line.find('-')
        min = int(line[0:idx1])
        idx2 = line.find(' ')
        max = int(line[idx1+1:idx2])
        char = line[idx2+1]
        password = line[line.find(' ',idx2+1)+1:]
        if (password[min-1] == char and password[max-1] != char) or (password[min-1] != char and password[max-1] == char):
            valid += 1
        # if password.count(char) >= min and password.count(char) <= max:
        #         valid += 1
print(valid)