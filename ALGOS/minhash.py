import random

def hash_word(word):
    if type(word)==str:
        return sum(ord(c) for c in word)
    else:
        return word # и не только word

def minhash(h, a, b, p=1010):
    return min(((a * hash_word(x) + b) % p) for x in h)

def compare_minhash(h1, h2, n=100):
    same = 0
    for _ in range(n):
        a, b = random.randint(1, 1000), random.randint(0, 1000)
        if minhash(h1, a, b) == minhash(h2, a, b):
            same += 1
    return same / n

def jaccard_similarity(set1, set2):
    return len(set1 & set2) / len(set1 | set2)


h1 = {"1", "мыло", "3", "Ржевский"}
h2 = {"телеввизор", "мыло", "Порутчик", "Ржевский"}

print(jaccard_similarity(h1, h2)/compare_minhash(h1,h2))


