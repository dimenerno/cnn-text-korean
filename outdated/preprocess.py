from random import shuffle

f = open("review_neg.txt", 'r', encoding='utf-8')
g = open("review_pos.txt", 'r', encoding='utf-8')
h = open("kkk.train", 'w', encoding='utf-8')

for i in f.readlines():
    h.write(i.strip() + '|neg\n')
for j in g.readlines():
    h.write(j.strip() + '|pos\n')


h.close()
h = open("kkk.train", 'r', encoding='utf-8')
sentences = h.readlines()
shuffle(sentences)

h.close()
h = open("kkk.train", 'w', encoding='utf-8')

for sentence in sentences:
    h.write(str(sentence))

f.close()
g.close()
h.close()
