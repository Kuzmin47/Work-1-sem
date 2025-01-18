def generate_subsets(elements):
    unique_elements = list(set(elements))
    def backtrack(start, path):
        if path:
            subsets.append(path)
        for i in range(start, len(unique_elements)):
            backtrack(i + 1, path + [unique_elements[i]])
    subsets = []
    backtrack(0, [])
    
    return len(subsets), subsets
elements = ['a','b','d','d','c']
count, subsets = generate_subsets(elements)
print("Подмножества:", subsets)
print("Количество подмножеств:", count)