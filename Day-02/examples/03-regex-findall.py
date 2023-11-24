import re

text = "The quick brown fox"
pattern = r"brown"

findall = re.findall(pattern, text)
if findall:
    print("Pattern found:", findall)
else:
    print("Pattern not found")
