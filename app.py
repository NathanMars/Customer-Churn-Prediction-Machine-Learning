# Genero -> 1 = Feminino, 2 = Masculino
# Churn -> 1 = Sim, 2 = Não
# O Scaler é exportado como scaler.pkl
# O modelo ideal para o problema é identificado no Jupiter Notebook e exportado como model.pkl
# A ordem dos dados em X são Age', 'Gender', 'Tenure', 'MonthlyCharges'

import joblib
import streamlit as st
import numpy as np

scaler = joblib.load("scaler.pkl")
model = joblib.load("model.pkl")

# Criaremos uma interface para que o usuário possa interagir com o modelo.
st.title("Previsor de Churn")

st.divider()

st.write("Por favor, informe os valores e aperte o botão para receber sua previsão")

st.divider()

age = st.number_input("Informe a Idade", min_value = 18, max_value=100, value=25)

tenure = st.number_input("Informe o tempo de uso do serviço", min_value = 0, max_value = 130, value = 10)

monthlycharge = st.number_input("Informe o valor da Cobrança Mensal", min_value = 30, max_value = 150)

gender = st.selectbox("Informe o genero", ("Masculino", "Feminino"))

st.divider()

predictbutton = st.button("Prever!")

st.divider()

if predictbutton:
    gender_selected = 1 if gender == "Feminino" else 0

    X = [age, gender_selected, tenure, monthlycharge]

    X1 = np.array(X)

    X_array = scaler.transform([X1])

    prediction = model.predict(X_array)[0]

    predicted = "SIM, Churn provavel!" if prediction == 1 else "NÃO, Churn improvavel!"

    st.write(f"Previsão: {predicted}")

else:
    st.write("Por favor, informe valores validos antes de apertar o botão")