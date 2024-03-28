
N = int(input())
words = [[] for _ in range(51)]
for _ in range(N):
    word = input()
    if word not in words[len(word)]:
        words[len(word)].append(word)
result = []
for word in words:
    if word:
        word.sort()
        print("\n".join(word))

