# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 00:21:02 2024

@author: tejas
"""
import os
import numpy as np
import pickle
import streamlit as st
from streamlit_option_menu import option_menu
# loading the saved model
kidney_model = pickle.load(open('F:/VIT FOLDER/CAPSTONE/proj/Trained models/kidney_model.sav', 'rb'))

heart_model = pickle.load(open('F:/VIT FOLDER/CAPSTONE/proj/Trained models/heart_model.sav', 'rb'))

liver_model = pickle.load(open('F:/VIT FOLDER/CAPSTONE/proj/Trained models/liver_model.sav', 'rb'))


# sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',

                           ['Kidney Prediction',
                            'Heart Disease Prediction',
                            'Liver Prediction'],
                           menu_icon='hospital-fill',
                           icons=['activity', 'heart', 'person'],
                           default_index=0)


# kidney Prediction Page

if selected == 'Kidney Prediction':

    # page title
    st.title('Kidney Prediction using ML')

    # getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        Age = st.text_input('Age')

    with col2:
        bp = st.text_input('bp')

    with col3:
        sg = st.text_input('sg')

    with col1:
        al = st.text_input('al')

    with col2:
        su = st.text_input('su')

    with col3:
        rbc = st.text_input('rbc')

    with col1:
        pc = st.text_input('pc')

    with col2:
        ppc = st.text_input('ppc')
    
    with col3:
        ba = st.text_input('ba')

    with col1:
        bgr = st.text_input('bgr')

    with col2:
        bu = st.text_input('bu')

    with col3:
        sc = st.text_input('sc')
        
    with col1:
        sod = st.text_input('sod')

    with col2:
        pot = st.text_input('pot')
    
    with col3:
        hemo = st.text_input('hemo')
        
    with col1:
        pvc = st.text_input('pvc')

    with col2:
        wc = st.text_input('wc')
    
    with col3:
        rc = st.text_input('rc')
        
    with col1:
        htn = st.text_input('htn')

    with col2:
        dm = st.text_input('dm')
    
    with col3:
        cad = st.text_input('cad')
        
    with col1:
        appet = st.text_input('appet')

    with col2:
        pe = st.text_input('pe')
    
    with col3:
        ane = st.text_input('ane')
        
    # code for Prediction
    kidney_diagnosis = ''

    # creating a button for Prediction

    if st.button('Kidney Disease Test Result'):

        user_input = [Age, bp, sg, al, su, rbc, pc, ppc, ba, bgr, bu, sc, sod, pot, hemo, pvc, wc, rc, htn, dm, cad, appet, pe, ane]

        user_input = [float(x) for x in user_input]

        kidney_prediction = kidney_model.predict([user_input])

        if kidney_prediction[0] == 1:
            kidney_diagnosis = 'The person is having kidney disease'
        else:
            kidney_diagnosis = 'The person does not have any kidney disease'

    st.success(kidney_diagnosis)






# Heart Prediction Page

if selected == 'Heart Disease Prediction':

    # page title
    st.title('Heart Prediction using ML')

    # getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')

    with col2:
        sex = st.text_input('Gender(male=1,female=0)')

    with col3:
        cp = st.text_input('Chest Pain types')
        
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')

    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')

    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')

    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')

    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')

    with col3:
        exang = st.text_input('Exercise Induced Angina')

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')

    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')

    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')

    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

    # code for Prediction
    heart_diagnosis = ''

    # creating a button for Prediction

    if st.button('Heart Disease Test Result'):

        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

        user_input = [float(x) for x in user_input]

        heart_prediction = heart_model.predict([user_input])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease (1)'
        else:
            heart_diagnosis = 'The person does not have any heart disease (0)'

    st.success(heart_diagnosis)


# Liver Prediction Page

if selected == 'Liver Prediction':

    # page title
    st.title('Liver Prediction using ML')

    # getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')

    with col2:
        gender= st.text_input('Gender(male=1, Female=2)')

    with col3:
        Total_Bilirubin = st.text_input('Total_Bilirubin')

    with col1:
        Direct_Bilirubin = st.text_input('Direct_Bilirubin')

    with col2:
        Alkaline_Phosphotase = st.text_input(' Alkaline_Phosphotase')

    with col3:
        Alamine_Aminotransferase = st.text_input('Alamine_Aminotransferase')

    with col1:
        Aspartate_Aminotransferase = st.text_input('Aspartate_Aminotransferase')

    with col2:
        Total_Protiens = st.text_input('Total_Protiens')

    with col3:
        Albumin = st.text_input('Albumin')

    with col1:
    	Albumin_and_Globulin_Ratio = st.text_input('Albumin_and_Globulin_Ratio')

    

    # code for Prediction
    liver_diagnosis = ''

    # creating a button for Prediction

    if st.button('Liver Disease Test Result'):

        user_input = [age, gender, Total_Bilirubin, Direct_Bilirubin, Alkaline_Phosphotase, Alamine_Aminotransferase, Aspartate_Aminotransferase, Total_Protiens, Albumin, Albumin_and_Globulin_Ratio]

        user_input = [float(x) for x in user_input]

        liver_prediction = liver_model.predict([user_input])

        if liver_prediction[0] == 1:
            liver_diagnosis = 'The person is having liver disease (1)'
        else:
            liver_diagnosis = 'The person does not have any liver disease (2)'

    st.success(liver_diagnosis)

