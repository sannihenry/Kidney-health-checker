# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 04:30:05 2024

@author: Sanni Henry
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 04:30:05 2024

@author: Sanni Henry
"""



import streamlit as st
from PIL import Image
image = Image.open('kidney_image.jpeg')
st.image(image, caption='Kidney: Everyday is a good day to take care of your Kidney')

import numpy as np
import pickle
import pandas as pd
#from flasgger import Swagger
import streamlit as st 

from PIL import Image

#app=Flask(__name__)
#Swagger(app)

pickle_in = open("Cclassifier.pkl","rb")
classifier=pickle.load(pickle_in)

#@app.route('/')
def welcome():
    return "Welcome All"

#@app.route('/predict',methods=["Get"])
def predict_note_authentication(age, blood_pressure, specific_gravity, albumin, sugar, red_blood_cells, pus_cell,
              pus_cell_clumps, bacteria, blood_glucose_random, blood_urea, serum_creatinine, sodium,
              potassium, haemoglobin, packed_cell_volume, white_blood_cell_count, red_blood_cell_count,
              hypertension, diabetes_mellitus, coronary_artery_disease, appetite, peda_edema,
              aanemia):

    """Let's Authenticate the Banks Note 
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: age
        in: query
        type: number
        required: true
      - name: blood_pressure
        in: query
        type: number
        required: true
      - name: specific_gravity
        in: query
        type: number
        required: true
      - name: albumin
        in: query
        type: number
        required: true
      - name: sugar
        in: query
        type: number
        required: true
      - name: red_blood_cells
        in: query
        type: number
        required: true
      - name: pus_cell
        in: query
        type: number
        required: true
      - name: potassium
        in: query
        type: number
        required: true
      - name: haemoglobin
        in: query
        type: number
        required: true
      - name: packed_cell_volume
        in: query
        type: number
        required: true
      - name: white_blood_cell_count
        in: query
        type: number
        required: true
      - name: red_blood_cell_count
        in: query
        type: number
        required: true
      - name: hypertension
        in: query
        type: number
        required: true
      - name: diabetes_mellitus
        in: query
        type: number
        required: true
      - name: coronary_artery_disease
        in: query
        type: number
        required: true
      - name: appetite
        in: query
        type: number
        required: true
      - name: peda_edema
        in: query
        type: number
        required: true
      - name: aanemia
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values
        
    """
   
    prediction=classifier.predict([[age, blood_pressure, specific_gravity, albumin, sugar, red_blood_cells, pus_cell,
              pus_cell_clumps, bacteria, blood_glucose_random, blood_urea, serum_creatinine, sodium,
              potassium, haemoglobin, packed_cell_volume, white_blood_cell_count, red_blood_cell_count,
              hypertension, diabetes_mellitus, coronary_artery_disease, appetite, peda_edema,
              aanemia]])
    print(prediction)
    return prediction



def main():
    st.title("Chronic Kidney Disease Prediction")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Check your Kidney health status </h2>
    </div>

    <div style="background-color:tomato;padding:10px">
    <h3 style="color:yellow;text-align:left;">Result: </h3>
    </div>    

    <div style="background-color:tomato;padding:5px">
    <h4 style="color:yellow;text-align:left;">ckd-Chronic Kidney Disease </h4>
    </div>    

    <div style="background-color:tomato;padding:5px">
    <h5 style="color:yellow;text-align:left;">Nckd-No Chronic Kidney Disease </h5>
    </div>    
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    age = st.text_input("age","Type Here")
    blood_pressure = st.text_input("blood_pressure","Type Here")
    specific_gravity = st.text_input("specific_gravity","Type Here")
    albumin = st.text_input("albumin","Type Here")
    sugar = st.text_input("sugar","Type Here")
    red_blood_cells = st.text_input("red_blood_cells","Type Here")
    pus_cell = st.text_input("pus_cell","Type Here")
    pus_cell_clumps = st.text_input("pus_cell_clumps","Type Here")
    bacteria = st.text_input("bacteria","Type Here")
    blood_glucose_random = st.text_input("blood_glucose_random","Type Here")
    blood_urea = st.text_input("blood_urea","Type Here")
    serum_creatinine = st.text_input("serum_creatinine","Type Here")
    sodium = st.text_input("sodium","Type Here")
    potassium = st.text_input("potassium","Type Here")
    haemoglobin = st.text_input("haemoglobin","Type Here")
    packed_cell_volume = st.text_input("packed_cell_volume","Type Here")
    white_blood_cell_count = st.text_input("white_blood_cell_count","Type Here")
    red_blood_cell_count = st.text_input("red_blood_cell_count","Type Here")
    hypertension = st.text_input("hypertension","Type Here")
    diabetes_mellitus = st.text_input("diabetes_mellitus","Type Here")
    coronary_artery_disease = st.text_input("coronary_artery_disease","Type Here")
    peda_edema = st.text_input("peda_edema","Type Here")
    aanemia = st.text_input("aanemia","Type Here")
    Gender = st.text_input("Gender","input (1) for male and (0) for female")
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(age, blood_pressure, specific_gravity, albumin, sugar, red_blood_cells, pus_cell,
              pus_cell_clumps, bacteria, blood_glucose_random, blood_urea, serum_creatinine, sodium,
              potassium, haemoglobin, packed_cell_volume, white_blood_cell_count, red_blood_cell_count,
              hypertension, diabetes_mellitus, coronary_artery_disease, appetite, peda_edema,
              aanemia)
    st.success('Your Kidney Health Status {}'.format(result))
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built by Henry")

if __name__=='__main__':
    main()
    
    
    