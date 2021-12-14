with open("Inputs/pinput10.txt") as f:
    # ses = 0
    acts = []
    for line in f:
        stack = []
        for char in line:
            if char == '(' or char == '[' or char == '{' or char == '<':
                stack.append(char)
            elif (char == ')' and stack[-1] == '(') or (char == ']' and stack[-1] == '[') or (char == '}' and stack[-1] == '{') or (char == '>' and stack[-1] == '<'):
                stack.pop()
            elif char == ')' or char == ']' or char == '}' or char == '>':
                stack = []
                break
        if stack:
            #print(line,"|",*stack)
            acts.append(0)
            for i in range(len(stack)):
                if stack[-1] == '(':
                    acts[-1] = acts[-1]*5+1
                    stack.pop()
                elif stack[-1] == '[':
                    acts[-1] = acts[-1]*5+2
                    stack.pop()
                elif stack[-1] == '{':
                    acts[-1] = acts[-1]*5+3
                    stack.pop()
                elif stack[-1] == '<':
                    acts[-1] = acts[-1]*5+4
                    stack.pop()
            print(*stack)
    acts.sort()
    #mid = int((len(acts)-1)/2)
    print(*acts)
    print(acts[25])



    #         elif char == ')':
    #             ses += 3
    #             break
    #         elif char == ']':
    #             ses += 57
    #             break
    #         elif char == '}':
    #             ses += 1197
    #             break
    #         elif char == '>':
    #             ses += 25137
    #             break
    # print(ses)