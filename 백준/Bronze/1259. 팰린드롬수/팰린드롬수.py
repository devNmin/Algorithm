
while True:
    word = input()
    if word == "0":
        break
    if len(word) % 2 == 0:
        middle = len(word)//2
        left = word[0:middle]
        right = word[middle::][-1::-1]
        if left == right:
            print('yes')
        else:
            print('no')
    else:
        middle = len(word)//2
        left = word[0:middle]
        right = word[middle+1::][-1::-1]
        if left == right:
            print('yes')
        else:
            print('no')
