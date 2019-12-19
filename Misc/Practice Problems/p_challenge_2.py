"""
p_challenge_2.py
"""

data = open("p_challenge_2.txt").read()
count = {}
for c in data:
    count[c] = count.get(c,0) + 1

print(count)
print(count.keys())