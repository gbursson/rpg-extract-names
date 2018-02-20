from bs4 import BeautifulSoup

"""file = open("files/001.txt", "r", encoding="utf-8")"""

file = open("files/Grombelardzka_legenda_split_005.html", "r", encoding="utf-8")

text = ""

for line in file:
    htmltxt = BeautifulSoup(line, "html.parser")
    text = text + htmltxt.get_text()


text = line.split(" ")
text = list(filter(lambda x: x != '', text))
text = list(filter(lambda x: x.istitle(), text))
text = list(filter(lambda x: len(x) != 1, text))

text = set(text)
text = sorted(list(text))


for word in text:
    print(word)





