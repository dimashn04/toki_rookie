wild, n = input(), int(input())

list_words = []
for i in range(n):
    word = input()
    list_words.append(word)

new = []
for word in list_words:
    if wild.find('*') == 0:
        if str(word).endswith(wild[wild.find('*')+1:]):
            new.append(word)
    elif wild.find('*') == len(wild) - 1:
        if str(word).startswith(wild[:wild.find('*')]):
            new.append(word)
    else:
        left, right = wild.split('*')

        if str(word).startswith(left) and str(word).endswith(right) and len(left+right) <= len(word):
            new.append(word)
            
for word in new:
    print(word)
