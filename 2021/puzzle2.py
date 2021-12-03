# with open("Inputs/pinput2.txt") as f:
#     pos = depth = val = 0
#     for line in f:
#         val = int(line[-2:-1])
#         if "forward" in line:
#             pos += val
#         if "down" in line:
#             depth += val
#         if "up" in line:
#             depth -= val
#     print(pos*depth)



with open("Inputs/pinput2.txt") as f:
    pos = depth = aim = val = 0
    for line in f:
        val = int(line[-2:-1])
        if "forward" in line:
            pos += val
            depth += aim*val
        if "down" in line:
            aim += val
        if "up" in line:
            aim -= val
    print(pos*depth)