from collections import Counter
s = "Из входной строки определить 3 наиболее часто встречаемых символа в ней."
def top3(s):
    counter = Counter(c for c in s if c != ' ')
    return counter.most_common(3)

print(top3(s))