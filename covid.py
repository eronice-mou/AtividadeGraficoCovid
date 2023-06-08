import streamlit as st
import pandas as pd
import numpy as np
from pandas import read_csv
from csv import DictReader


st.title('Dashboard')
st.markdown('''## Análise dos dados das vacinas da Covid 19''')



if st.button('Visualisar de tabela'):
    arquivo = read_csv("vaccination-data.csv")
    st.write(arquivo)



agree = st.checkbox('ver gráfico')

if agree:

    d = {'TOTAL_VACCINATION': ['15,203,606', '3,080,679', '15,267,442', '114,706'], 'PERSON_VACCINED_1PLUS_DOSE': ['15,203,606', '1,348,396', '7,840,131', '46,206']}
    df = pd.DataFrame(d)
    st.line_chart(df)
    st.write(df)