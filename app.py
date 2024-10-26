import pandas as pd 
import plotly_express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv') # leer los datos
st.header('Anuncio de ventas de coches')
hist_button = st.button('Construir histograma') # crear un botón
second_button = st.button('construir grafico') # crear segundo grafico

if hist_button: # al hacer clic en el botón
            # escribir un mensaje
            st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
            # crear un histograma
            fig = px.histogram(car_data, x="odometer")
        
            # mostrar un gráfico Plotly interactivo
            st.plotly_chart(fig, use_container_width=True)

if second_button: #clikear el boton
        st.write('Creacion del grafico de disperción')

        #crear grafico de dispercion 
        figs = px.scatter(car_data, x='model_year', y='price', title="Gráfico de Dispersión")
        st.plotly_chart(figs, use_container_width=True)

        


