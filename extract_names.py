from bs4 import BeautifulSoup
import re
import operator

file = open("files/a.html", "r", encoding="utf-8")

text = BeautifulSoup(file, "html.parser").get_text()
text = text.split(" ")


new_list = []
for word in text:
    word = re.sub('[!,()„*.\d+?—]', '', word)
    new_list.append(word)

text = new_list

text = list(filter(lambda x: x != '', text))
text = list(filter(lambda x: x.istitle(), text))
text = list(filter(lambda x: (len(x) != 1 and len(x) != 2), text))

text = set(text)
text = sorted(list(text))

print(text)

"""
for word in text:
    print(word)
"""
