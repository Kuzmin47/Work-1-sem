s = str(input())
n = s.count('  ')
s = s.split()
a = {}
for i in range(len(s)):
    a[str(sorted(s[i]))] = a.get(str(sorted(s[i])), []) + [s[i]]
a[''] = ['']*n
a.pop('')
print(*a.values(), sep='\n')

