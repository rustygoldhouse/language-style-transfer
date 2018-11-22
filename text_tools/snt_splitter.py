import re

text = ''.join(open('kafka.txt').readlines())

new_text = text.replace('\n', '')

sentences = re.split(r' *[\.\?!][\'"\)\]]* *', new_text)


new_lined = '.\n'.join(sentences)

file = open('other_model.txt', 'w')

file.write(new_lined)