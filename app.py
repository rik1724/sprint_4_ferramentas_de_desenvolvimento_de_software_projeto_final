# Importando as bibliotecas necessárias
import pandas as pd
import plotly.express as px
import streamlit as st

# Carregando os dados do arquivo CSV
car_data = pd.read_csv('vehicles.csv')

# Criando um cabeçalho
st.header('Análise Exploratória de Dados')

# Botão para criar um histograma
hist_button = st.button('Criar histograma para o odômetro')

if hist_button:  # Se o botão for clicado
    st.write('Criando um histograma para o odômetro')
    fig = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig, use_container_width=True)

# Botão para criar um gráfico de dispersão
scatter_button = st.button('Criar gráfico de dispersão')

if scatter_button:  # Se o botão for clicado
    st.write('Criando um gráfico de dispersão')
    fig = px.scatter(car_data, x='odometer', y='price')
    st.plotly_chart(fig, use_container_width=True)

