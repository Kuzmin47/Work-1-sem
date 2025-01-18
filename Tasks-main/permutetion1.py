res = set()
def findPermutations(string, i = 0):
    if i == len(string):
        s_string = "".join(string)
        if s_string not in res:   	 
            print("".join(string))
            res.add(s_string)

    for j in range(i, len(string)):
        words = [c for c in string]
        words[i], words[j] = words[j], words[i]
        findPermutations(words, i + 1)
string = str(input())
findPermutations(string)