from random import shuffle

f = open("review_neg_cls.txt", 'r')
g = open("review_pos_cls.txt", 'r')
h = open("kkk.dev", 'w')

print(f.readline())

for i in f.readlines():
    h.write(i.strip() + '`neg\n')
for j in g.readlines():
    h.write(j.strip() + '`pos\n')


h.close()
h = open("kkk.dev", 'r')
sentences = h.readlines()
shuffle(sentences)

h.close()
h = open("kkk.dev", 'w')

for sentence in sentences:
    h.write(str(sentence))

f.close()
g.close()
h.close()
