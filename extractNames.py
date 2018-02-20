file = open("files/001.txt", "r", encoding="utf-8")

for line in file:
    text = line.split(" ")

text = list(filter(lambda x: x != '', text))
text = list(filter(lambda x: x.istitle(), text))
text = list(filter(lambda x: len(x) != 1, text))

text = set(text)
text = sorted(list(text))


for word in text:
    print(word)