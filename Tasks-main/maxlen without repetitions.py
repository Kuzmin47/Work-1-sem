string = input()
lence = len(string)
pos = {}
m =[]
last = 0
for i in range(lence):
    if string[i] not in pos:
        pos[string[i]] = 1
    else:
        pos[string[i]] += 1
    if pos[string[i]] > 1:
        m.append(string[last:i])
        pos = {}
        last = i
        pos[string[i]] = 1
m.append(string[last:])
print(max(m, key=len))