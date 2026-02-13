def hash(word):
    hash_val = 0
    for char in word:
        hash_val += ord(char)
    return hash_val % 10

print(hash('usehashfunc'))
