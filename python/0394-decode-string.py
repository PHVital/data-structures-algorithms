def decodeString(s):
    stack = []
    current_num = 0
    current_string = ''

    for char in s:
        if char.isdigit():
            current_num = current_num * 10 + int(char)
        elif char == '[':
            stack.append((current_string, current_num))
            current_string = ''
            current_num = 0
        elif char == ']':
            prev_string, repeat = stack.pop()
            current_string = prev_string + current_string * repeat
        else:
            current_string += char
    return current_string


print(decodeString('3[a]2[bc]'))

# 3[a]2[bc] 3[a2[c]]