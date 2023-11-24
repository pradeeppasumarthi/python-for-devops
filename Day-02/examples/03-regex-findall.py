import re

text = "The quick brown fox"
pattern = r"brown"

findall = re.findall(pattern, text)
if findall:
    print("Pattern found:", search)
else:
    print("Pattern not found")
