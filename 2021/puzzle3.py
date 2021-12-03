# with open("Inputs/pinput3.txt") as f:
#     zeros = [0,0,0,0,0,0,0,0,0,0,0,0]
#     ones = [0,0,0,0,0,0,0,0,0,0,0,0]
#     for line in f:
#         for i in range(0,len(line)-1):
#             if line[i] == '0':
#                 zeros[i] += 1
#             else:
#                 ones[i] += 1
#     gamma = ""
#     epsilon = ""
#     for i in range(0,12):
#         if zeros[i] > ones[i]:
#             gamma += '0'
#             epsilon += '1'
#         else:
#             gamma += '1'
#             epsilon += '0'

# gamma = 0b101001100111
# epsilon = 0b010110011000
# print(int(gamma)*int(epsilon))



# cparr = []
# with open("Inputs/pinput3.txt") as f:
#     for line in f:
#         cparr.append(line)
# ogr = csr = "0b"
# srch = 0
# while srch < 12:
#     common = [0,0,0,0]
#     for num in cparr:
#         if ogr[2:] in num[:srch] and num[srch] == '0':
#             common[0] += 1
#         elif ogr[2:] in num[:srch] and num[srch] == '1':
#             common[1] += 1
#         if csr[2:] in num[:srch] and num[srch] == '0':
#             common[2] += 1
#         elif csr[2:] in num[:srch] and num[srch] == '1':
#             common[3] += 1
#     # print(*common)
#     if common[0] > common[1]:
#         ogr += '0'
#     else:
#         ogr += '1'
#     if common[2] <= common[3]:
#         csr += '0'
#     else:
#         csr += '1'
#     srch += 1
# print(int(ogr,2)*int(csr,2))
print(int('0b100111011110',2)*int('010010100000',2))