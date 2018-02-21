from bs4 import BeautifulSoup
import re

input_file = open("files/a.html", "r", encoding="utf-8")

text = BeautifulSoup(input_file, "html.parser").get_text()
input_file.close()

text = text.split(" ")

# apply set of filters to the list (remove - empty, non-names and 1 or 2 characters)
text = list(filter(lambda x: x != '', text))
text = list(filter(lambda x: x.istitle(), text))
text = list(filter(lambda x: (len(x) != 1 and len(x) != 2), text))

# regexp non-letter characters

new_list = []
for word in text:
    word = re.sub('[!,()„*.\d+?—“”:;]', '', word)
    new_list.append(word)
text = new_list

text = set(text)
text = sorted(list(text))

output_file = open("namex.txt", "w+", encoding="utf-8")

for word in text:
    output_file.write(word + "\n")

output_file.close()
