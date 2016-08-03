import re

text = "A cat and a rat can't be friends."
partern = "cat"

result = re.search(partern, text)

print result
print result.start()
print result.end()
print text[result.start():result.end()]

partern = "[dt]"

result = re.search(partern, text)

print result
print result.start()
print result.end()