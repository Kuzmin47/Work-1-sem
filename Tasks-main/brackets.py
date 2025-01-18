m = []
def line_correction(string: str):
    if string != '':
        while string[-1] == '(' or string [-1] == '{' or string [-1] == '[':
            string = string[:-1]
    return string
def invalid(s: str):
    stack = []
    hm = { ")" : "(", "}" : "{", "]" : "["}
    string = ''
    correct_parenthesis_sequence = 0
    for c in range(len(s)):
        if s[c] in hm:
            if stack and stack[-1] == hm[s[c]]:
                stack.pop()
                string = string + s[c]
                correct_parenthesis_sequence = 1
            else:
                if correct_parenthesis_sequence == 0:
                    string = ''
                    stack = []
                else:
                    string = line_correction(string)
                    m.append(string)
                    string = ''
                    correct_parenthesis_sequence = 0
        else:
            stack.append(s[c])
            string = string + s[c]
    string = line_correction(string)
    m.append(string)
s = input()
invalid(s)
if m[0] == s:
    print(True)
elif m[0] != '':
    print(max(m,key=len))
else:
    print(False)