with open('46input.txt', mode='r') as hi:
    text = hi.read()

text = text.split()

words = []
for i in text:
    if i not in words:
        words.append(i)


def get_count(i):
    return i[0]

words_organised = {}
for word in words:
    occurrences = text.count(word)
    words_organised[word] = occurrences
    words_organised = dict(sorted(words_organised.items(), key=get_count)) # sorts list by count


for key, value in words_organised.items():
    stars = ''
    for i in range(value):
        stars += '*'
    print(f"{key}: {stars}")