import streamlit as st
import pandas as pd
import joblib  

model = joblib.load('approval_pred_best_model.pkl')  

employment_mappings = {' No': 0, ' Yes': 1}
education_mappings = {' Graduate': 0, ' Not Graduate': 1}
approval_mappings = {0: 'Approved', 1: 'Rejected'}

employment = list(employment_mappings.keys())
education = list(education_mappings.keys())

st.title("Approval Prediction")


Dependents = int(st.text_input("Number of dependents", "2"))
Education = st.selectbox("Education", education)
Employment = st.selectbox("Self Employment", employment)
Inc = int(st.text_input("Income (per annum)", "40000"))
Am = int(st.text_input("Loan Amount", "5000"))
Ter = float(st.text_input("Loan Term (years)", "3.5"))
Score = int(st.text_input("Credit Score", "670"))
Res_assets_val = int(st.text_input("Residential Assets Value", "500000"))
Com_assets_val = int(st.text_input("Commercial Assets Value", "10000"))
Lux_assets_val = int(st.text_input("Luxury Assets Value", "10000"))
Bank_assets_val = int(st.text_input("Bank Assets Value", "15000"))

encoded_emp = employment_mappings[Employment]
encoded_ed = education_mappings[Education]

if st.button("Predict Approval"):
    input_data = pd.DataFrame({
        ' no_of_dependents': [Dependents], 
        ' education': [encoded_ed], 
        ' self_employed': [encoded_emp], 
        ' income_annum': [Inc], 
        ' loan_amount': [Am], 
        ' loan_term': [Ter], 
        ' cibil_score': [Score], 
        ' residential_assets_value': [Res_assets_val], 
        ' commercial_assets_value': [Com_assets_val], 
        ' luxury_assets_value': [Lux_assets_val], 
        ' bank_asset_value': [Bank_assets_val], 
    })

    predicted_score = model.predict(input_data)[0]
    prediction_category = approval_mappings[predicted_score]

    if predicted_score == 0:
        st.success(f"The approval prediction result is: {prediction_category}")
    elif predicted_score == 1:
        st.markdown(
            f"<p style='color:red; font-weight:bold;'>The approval prediction result is: {prediction_category}</p>", 
            unsafe_allow_html=True
        )
