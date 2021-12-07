# numvalid = 0
# with open("Inputs/pinput4.txt") as f:
#     fields = [False, False, False, False, False, False, False]
#     cum = ""
#     for line in f:
#         # print(line)
#         cum += line
#         if "byr" in line:
#             fields[0] = True
#         if "iyr" in line:
#             fields[1] = True
#         if "eyr" in line:
#             fields[2] = True
#         if "hgt" in line:
#             fields[3] = True
#         if "hcl" in line:
#             fields[4] = True
#         if "ecl" in line:
#             fields[5] = True
#         if "pid" in line:
#             fields[6] = True
#         if len(line) <= 1:
#             if fields[0] and fields[1] and fields[2] and fields[3] and fields[4] and fields[5] and fields[6]:
#                 # print("valid")
#                 numvalid += 1
#             else:
#                 print(cum)
#                 print(*fields)
#             # print("*******")
#             cum = ""
#             fields = [False, False, False, False, False, False, False]
# print(numvalid)



import string
import re

with open("Inputs/pinput4.txt") as f:
    arr = [re.compile('(?<=byr:)19[2-9][0-9]|(?<=byr:)200[0-2]'),
        re.compile('(?<=iyr:)201[0-9]|(?<=iyr:)2020'),
        re.compile('(?<=eyr:)202[0-9]|(?<=eyr:)2030'),
        re.compile('(?<=hgt:)1[5-8][0-9]cm|(?<=hgt:)19[0-3]cm|(?<=hgt:)59in|(?<=hgt:)6[0-9]in|(?<=hgt:)7[0-6]in'),
        re.compile('(?<=hcl:#)[0-9a-f]{6}'),
        re.compile('ecl:amb|ecl:blu|ecl:brn|ecl:gry|ecl:grn|ecl:hzl|ecl:oth'),
        re.compile('(?<=pid:)[0-9]{9}')]
    numvalid = 0
    cum = ""
    for line in f:
        if len(line) <= 1:
            valid = True
            for i in range(len(arr)):
                if arr[i].search(cum) == None:
                    valid = False
                    break
            if valid:
                numvalid += 1
            cum = ""
        else:
            cum += line
    print(numvalid)