import pandas as pd
import streamlit as st
import plotly.graph_objects as go
import plotly.express as px

st.set_page_config(page_title='Players 19')

st.write('<h1 style= "text-align: center;">Players Results 2019</h1>', unsafe_allow_html= True)
st.subheader('Abner Ribeiro, Data Analyst')

# LOAD DE DATA
df = pd.read_csv('players19.csv')
df.index += 1

container = st.container()

# inserir o dataframe no container
with container:
    st.dataframe(df.style.set_properties(**{'text-align': 'center'}), width=800)


# Filtrando os dados por nacionalidade
nationality = df['Nationality'].value_counts().iloc[:10]
position = df['Position'].value_counts().iloc[:10]
df_nationality = pd.Series(nationality)
df_position = pd.Series(position)

grafico = go.Bar(x=df_nationality.index, y=df_nationality.values, marker= dict(color= '#F63366'))

layout = go.Layout(
    title='10 seleções com maior número de jogadores',
    xaxis=dict(title='Seleções'),
    yaxis=dict(title='Índice'),

)

# Renderizar o gráfico
st.plotly_chart(go.Figure(data=[grafico], layout=layout))

#Classificação por posição


grafico_ps = go.Bar(x=df_position.index, y=df_position.values, marker= dict(color= '#0094c6'))

layout_ps = go.Layout(
    title='10 posições com maior número de jogadores',
    xaxis=dict(title='Posições'),
    yaxis=dict(title='Índice'),

)

# Renderizar o gráfico
st.plotly_chart(go.Figure(data=[grafico_ps], layout=layout_ps))


#Correlação dos dados
corr = df.corr(numeric_only=True)

heatmap = go.Heatmap(z= corr.values, x= corr.index.values, y = corr.columns.values)
layout_heat = go.Layout(title= 'Heatmap de correlação')
fig_heat= go.Figure(data=[heatmap], layout= layout_heat)

st.plotly_chart(go.Figure(data=[heatmap], layout=layout_heat))


