import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


pr = pd.read_csv(
    './Formulário de Avaliação de egressos dos cursos Técnicos Subsequentes do IFB (respostas).csv',
    encoding='latin1',
    parse_dates=['Carimbo de data/hora', 'Data de nascimento:'],
    sep=';',
    decimal=',',
    thousands='.'
)
pr.plot.scatter(x="Carimbo de data/hora", y="Concluiu o seu curso no tempo previsto?", alpha=0.5)

x = [' ']
y = ['qwr']

st.title('Olá povo ')

plt.scatter(pr)
plt.show()


st.pyplot(plt)

