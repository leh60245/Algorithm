k = input().upper()
word = []
cnt = []
for i in k:
    if i not in word:
        word.append(i)
        cnt.append(1)
        continue
    cnt[word.index(i)] += 1

if cnt.count(max(cnt)) >= 2:
    print("?")
else:
    print(word[cnt.index(max(cnt))])