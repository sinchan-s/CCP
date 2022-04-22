import json
import pickle
import numpy as np

__article = None
__fibre = None
__finish = None
__prints = None
__data_columns = None
__model = None


def get_estimated_consum(article,fibre,finish,prints,count,cover,meters,mesh,rod,speed,hits,c_hits,viscosity,machine):
    try:
        art_index = __data_columns.index(article.lower())
    except:
        art_index = -1
    try:
        fib_index = __data_columns.index(fibre.lower())
    except:
        fib_index = -1
    try:
        fin_index = __data_columns.index(finish.lower())
    except:
        fin_index = -1
    try:
        sty_index = __data_columns.index(prints.lower())
    except:
        sty_index = -1
    x = np.zeros(len(__data_columns))
    x[0] = count
    x[1] = cover
    x[2] = meters
    x[3] = mesh
    x[4] = rod
    x[5] = speed
    x[6] = hits
    x[7] = c_hits
    x[8] = viscosity
    x[9] = machine
    if art_index or fib_index or fin_index or sty_index > 0:
        x[art_index] = 1
        x[fib_index] = 1
        x[fin_index] = 1
        x[sty_index] = 1
    return round(__model.predict([x])[0], 2)


def get_article_names():
    global __article
    return __article

def get_fibre_names():
    global __fibre
    return __fibre

def get_finish_names():
    global __finish
    return __finish

def get_prints_names():
    global __prints
    return __prints

def load_saved_artifacts():
    print('loading saved artifacts...start')
    global __article
    global __fibre
    global __prints
    global __finish
    global __data_columns
    global __model
    with open('./artifacts/columns.json', 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __article = __data_columns[10:107]
        __fibre = __data_columns[107:117]
        __finish = __data_columns[117:120]
        __prints = __data_columns[120:]

    with open('./artifacts/color_model.pickle', 'rb') as f:
        __model = pickle.load(f)
    print('loading saved artifacts...done')


if __name__ == "__main__":
    load_saved_artifacts()
    print(get_article_names())
    print(get_fibre_names())
    print(get_finish_names())
    print(get_prints_names())
    print(get_estimated_consum('18006','Ct','none','reactive',30,40,1000,125,8,30,1,1,70,2))
