from tqdm import tqdm

def word_value(word):
    return sum([ord(ch) - 64 for ch in word])

with open("p042_words.txt", "r") as file:
    s = file.read()
    words = s.split(",")
    words = [word[1:-1] for word in words]



t = [int(0.5*n*(n+1)) for n in range(1000)]

counter = 0
for word in tqdm(words):
    if word_value(word) in t:
        counter += 1

print(counter)



