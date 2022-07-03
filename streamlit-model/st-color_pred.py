# important libraries
import streamlit as st
import numpy as np
import pickle
import sklearn

# site configurations
st.set_page_config(
    page_title="Color Consumption Prediction",
    page_icon="",
    initial_sidebar_state="expanded",
)

# info section
st.title('Color Consumption Predictor')
st.subheader("Input the values below to estimate the color consumption.")

# matplotlib colormap selection dropdown
articles_list = ("11600084", "116414", "12000251", "120109", "120G88", "120H89", "12400017", "13000391", "13000437", "130176", "130C56", "130D07", "130K00", "130Q28", "13200046", "132144", "132340", "13257", "132B147", "14000313", "14000396", "14000398", "14000756", "1400398", "140117", "14015", "140313", "140324", "140367", "140J17", "14500101", "150264", "150442", "150G07", "16000173", "16000314", "16009", "160A63", "18006", "A120A528", "A120B045", "A120B375", "A120C093", "A130A343", "A130B074", "A130B459", "A130B609", "A130B652", "A130B680", "A130C150", "A130D001", "A130D621", "A130K00", "A132A44", "A132A744", "A132A901", "A132A927", "A132B006", "A132B147", "A132B148", "A1400058", "A1400232", "A140A622", "A140C096", "A140C537", "A140C538", "A140D080", "A140D377", "A140D660", "A140D663", "A140D722", "A140E042", "A140E111", "A140E129", "A145A279", "A145A280", "A145A281", "A145A387", "A150B433", "A150B589", "A150B593", "A150C071", "A150C549", "A150C944", "A150C971", "A150D067", "A150D079", "A150D080", "A1600279", "A160A416", "A160A483", "A160A742", "A160B551", "A160B684", "A180A234", "A280A354", "A2A0A621")
styles_list = ("Pigment", "Reactive", "Discharge")
finish_list = ("None", "Peach", "Raise")
data_columns_list = np.array(["coverage", "meters", "mesh", "rod", "speed", "hits", "color-hits", "viscosity", "machine", "11600084", "116414", "12000251", "120109", "120g88", "120h89", "12400017", "13000391", "13000437", "130176", "130c56", "130d07", "130k00", "130q28", "13200046", "132144", "132340", "13257", "132b147", "14000313", "14000396", "14000398", "14000756", "1400398", "140117", "14015", "140313", "140324", "140367", "140j17", "14500101", "150264", "150442", "150g07", "16000173", "16000314", "16009", "160a63", "18006", "a120a528", "a120b045", "a120b375", "a120c093", "a130a343", "a130b074", "a130b459", "a130b609", "a130b652", "a130b680", "a130c150", "a130d001", "a130d621", "a130k00", "a132a44", "a132a744", "a132a901", "a132a927", "a132b006", "a132b147", "a132b148", "a1400058", "a1400232", "a140a622", "a140c096", "a140c537", "a140c538", "a140d080", "a140d377", "a140d660", "a140d663", "a140d722", "a140e042", "a140e111", "a140e129", "a145a279", "a145a280", "a145a281", "a145a387", "a150b433", "a150b589", "a150b593", "a150c071", "a150c549", "a150c944", "a150c971", "a150d067", "a150d079", "a150d080", "a1600279", "a160a416", "a160a483", "a160a742", "a160b551", "a160b684", "a180a234", "a280a354", "a2a0a621", "none", "peach", "raise", "discharge", "pigment", "reactive"])

col1, col2, col3 = st.columns(3)
meters = col1.number_input("Meters", min_value=1, max_value=100000)
coverage = col2.number_input("Coverage %", min_value=0.01, max_value=100.00)
article = col3.selectbox("Select an article", articles_list)
style = col1.selectbox("Choose the print style", styles_list)
finish = col2.selectbox("Greige Fabric finish", finish_list)
mesh = col3.selectbox("Screen Mesh", (125, 155, 165, 195))
speed = col1.slider("Speed", 10, 100)
viscosity = col2.slider("Color Paste Viscosity", 40, 200)
machine = col3.radio("Machine No.", (1, 2, 3), horizontal=True)
rod = col1.radio("Rod Size", (6, 8, 10, 12, 15, 20), horizontal=True)
hits = 1
c_hits = 1

# paste value calculated using empirical formula
cal_val = int(meters * coverage / 700 + 23)
cal = f'{cal_val} Kg'
st.subheader("Calculated Color Paste:")
st.latex(r'''Quantity = \left(\frac{Coverage × Meters}{700}\right) + 23 Kg''')
st.info(cal)

with open('../model/color_model.pickle', 'rb') as f:
    model = pickle.load(f)


def predict_consum(article, finish, style, coverage, meters, mesh, rod, speed, hits, c_hits, viscosity, machine):
    print('starting')
    try:
        art_index = np.where(data_columns_list == article.lower())[0][0]
    except:
        return 0
    try:
        fin_index = np.where(data_columns_list == finish.lower())[0][0]
    except:
        return 0
    try:
        sty_index = np.where(data_columns_list == style.lower())[0][0]
    except:
        return 0
    x = np.zeros(len(data_columns_list))
    x[0] = coverage
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
    return model.predict([x])[0]



pred_value = predict_consum(article, finish, style, coverage, meters, mesh, rod, speed, hits, c_hits, viscosity, machine)
st.subheader("Predicted Color Paste:")
pred = f'{pred_value} Kg'
st.info(pred)
