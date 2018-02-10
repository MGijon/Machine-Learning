import gensim.models as gm
import numpy as np

route = '/Users/manuelgijonagudo/Documents/Programación/GIT/Data/GoogleNews-vectors-negative300.bin.gz'
model = gm.KeyedVectors.load_word2vec_format(route, binary = True)

print(model.most_similar( positive = ['woman', 'king'], negative = ['man'], topn = 1))