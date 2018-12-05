from random import shuffle
from konlpy.tag import Kkma

f = open("outdated/review_neg_dev.txt", 'r')
g = open("outdated/review_pos_dev.txt", 'r')
h = open("outdated/kkk.dev", 'w')

kkma = Kkma()


def load_data_and_labels(sentence):
    li = [i[0] for i in kkma.pos(sentence)]
    my_str = ""
    for i in li:
        my_str += (i + ' ')
    return my_str


for i in f.readlines():
    h.write(load_data_and_labels(i) + '|neg\n')
for j in g.readlines():
    h.write(load_data_and_labels(j) + '|pos\n')

h.close()

h = open("outdated/kkk.dev", 'r')
sentences = h.readlines()
shuffle(sentences)

h.close()
h = open("outdated/kkk.dev", 'w')

for sentence in sentences:
    h.write(str(sentence))

f.close()
g.close()
h.close()
