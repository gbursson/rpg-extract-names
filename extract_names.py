from bs4 import BeautifulSoup
import re
import operator

file = open("files/a.html", "r", encoding="utf-8")

remove_text = "(),\„"
remove_list = list(remove_text)

text = BeautifulSoup(file, "html.parser").get_text()

text = text.split(" ")
text = sorted(list(text))

text = list(filter(lambda x: x != '', text))
text = list(filter(lambda x: x.istitle(), text))
text = list(filter(lambda x: len(x) != 1, text))
text = list(filter(lambda x: len(x) != 2, text))

print(text)



"""
for word in text:
    print(word)
"""
