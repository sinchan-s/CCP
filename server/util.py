import json
import pickle
import numpy as np

__article = None
__finish = None
__prints = None
__data_columns = None
__model = None


def get_estimated_consum(article,finish,prints,cover,meters,mesh,rod,speed,hits,c_hits,viscosity,machine):
    try:
        art_index = __data_columns.index(article.lower())
    except:
        art_index = -1
    try:
        fin_index = __data_columns.index(finish.lower())
    except:
        fin_index = -1
    try:
        sty_index = __data_columns.index(prints.lower())
    except:
        sty_index = -1
    x = np.zeros(len(__data_columns))
    x[0] = cover
    x[1] = meters
    x[2] = mesh
    x[3] = rod
    x[4] = speed
    x[5] = hits
    x[6] = c_hits
    x[7] = viscosity
    x[8] = machine
    if art_index or fin_index or sty_index > 0:
        x[art_index] = 1
        x[fin_index] = 1
        x[sty_index] = 1
    return round(__model.predict([x])[0], 2)


def get_article_names():
    global __article
    return __article

def get_finish_names():
    global __finish
    return __finish

def get_prints_names():
    global __prints
    return __prints

def load_saved_artifacts():
    print('loading saved artifacts...start')
    global __article
    global __prints
    global __finish
    global __data_columns
    global __model
    with open('./artifacts/columns.json', 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __article = __data_columns[9:106]
        __finish = __data_columns[106:109]
        __prints = __data_columns[109:]

    with open('./artifacts/color_model.pickle', 'rb') as f:
        __model = pickle.load(f)
    print('loading saved artifacts...done')


if __name__ == "__main__":
    load_saved_artifacts()
    print(get_article_names())
    print(get_finish_names())
    print(get_prints_names())
    print(get_estimated_consum('13200046','raise','pigment',40,1000,125,8,30,1,1,70,2))
