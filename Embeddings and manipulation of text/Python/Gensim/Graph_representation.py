import gensim.models as gm
import pandas as pd
import networkx as nx
from matplotlib import pyplot as plt

## Cargamos los datos:
## ===================

# ruta mac:
filepath = 'Data/words_source.csv'
# ruta windows:
# filepath = ''
data = pd.read_csv(filepath, sep = ';')
data.head()

data = data[['Pos1', 'R1', 'R2', 'R3', 'R4', 'R5']]

## Cargamos el modelo:
## ===================

# ruta mac:
route = '/Users/manuelgijonagudo/Documents/Programación/GIT/Data/GoogleNews-vectors-negative300.bin.gz'
# ruta windows:
# route = 'D:\GIT\Data\GoogleNews-vectors-negative300.bin.gz'
model = gm.KeyedVectors.load_word2vec_format(route, binary = True)

## Comenzamos con la representación:
## =================================

list_words_POS1 = []
list_words_R1 = []
list_words_R2 = []
list_words_R3 = []
list_words_R4 = []
list_words_R5 = []

# aquí añadimos a la lista de palabras los elementos en la posición 1
i = 0
while isinstance(data['Pos1'][i] , str):
    list_words_POS1.append(data.iloc[i]['Pos1'])
    list_words_R1.append(data.iloc[i]['R1'])
    list_words_R2.append(data.iloc[i]['R2'])
    list_words_R3.append(data.iloc[i]['R3'])
    list_words_R4.append(data.iloc[i]['R4'])
    list_words_R5.append(data.iloc[i]['R5'])
    i += 1


## =============================================================================
## Hasta aquí ya tenemos las palabras del csv organizadas en listas apropiadas,
## nos resta ponerlos es en formato correcto (I) y aplicarles la función para
## hacer la representación gráfica
## =============================================================================

def construct_word_dict(list):
    ''' Construimos un diccionario en el formato que necesitamos para el PCA '''
    dict = {}
    for i in list:
        dict[i] = model.wv.vocab[i]
    return dict
