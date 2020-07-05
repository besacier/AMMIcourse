from collections import defaultdict

word_counts = defaultdict(int)

for w in open('runbun_ilimi/runbin_ilimi.txt', encoding="utf-8").read().split():
    word_counts[w.lower()] += 1

totalCount = 0;
for w, c in word_counts.items():
    totalCount += 1
print(totalCount)