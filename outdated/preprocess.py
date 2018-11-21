from random import shuffle

f = open("outdated/rt-polarity.neg", 'r', encoding='UTF8')
g = open("outdated/rt-polarity.pos", 'r', encoding='UTF8')
h = open("outdated/kkk.train", 'w', encoding='UTF8')

for i in f.readlines():
    h.write(i.strip() + '+neg\n')
for j in g.readlines():
    h.write(j.strip() + '+pos\n')


h.close()
h = open("outdated/kkk.train", 'r', encoding='UTF8')
sentences = h.readlines()
shuffle(sentences)

h.close()
h = open("outdated/kkk.train", 'w', encoding='UTF8')

for sentence in sentences:
    h.write(str(sentence))

f.close()
g.close()
h.close()
