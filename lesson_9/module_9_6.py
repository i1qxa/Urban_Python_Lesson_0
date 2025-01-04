def all_variants(text):
    size = len(text)
    for start in range(size):
        for end in range(start + 1, size + 1):
            yield text[start:end]

print(list(all_variants('abc')))