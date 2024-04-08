N = int(input())
card1 = list(map(int, input().split()))

M = int(input())
card2 = list(map(int, input().split()))
card_dict = {}
for a in card1:
    if a not in card_dict:
        card_dict[a] = 1
    else:
        card_dict[a] += 1
ans = []
for card in card2:
    ans.append(card_dict.get(card, 0))
print(*ans)
