# important libraries
import streamlit as st
import numpy as np

#import matplotlib.pyplot as plt

#from sklearn.pipeline import Pipeline
#from sklearn.preprocessing import PolynomialFeatures, StandardScaler


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
finish_list = ("NF", "Peach(P)", "Reactive(R)")

#st.subheader('Parameters entered: ')
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
hits = col2.radio("Samples printed", (1, 2, 3, 4, 5), horizontal=True)
c_hits = col1.radio("Max Color Hits", (1, 2, 3, 4, 5), horizontal=True)

# paste value calculated using empirical formula
cal_val = int(meters*coverage/700+23)
emp_value = f'{cal_val} Kg'

st.subheader("Calculated Color Paste required:")
st.latex(r'''
 \left(\frac{Coverage × Meters}{700}\right) + 23 Kg''')
st.info(emp_value)

st.subheader("Estimated Color Paste required:")
st.info("prediction")