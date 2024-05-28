import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def calcular_vertice(a, b, c):
    if a == 0:
        return None
    x_vertice = -b / (2 * a)
    y_vertice = a * x_vertice ** 2 + b * x_vertice + c
    return x_vertice, y_vertice

def plot_funcao_segundo_grau(a, b, c):
    vertice = calcular_vertice(a, b, c)
    if vertice:
        x_vertice, y_vertice = vertice
        x_min = x_vertice - 10
        x_max = x_vertice + 10
        y_min = y_vertice - 10
        y_max = y_vertice + 10
    else:
        x_min, x_max = -10, 10
        y_min, y_max = -10, 10

    x = np.linspace(x_min, x_max, 400)
    y = a * x ** 2 + b * x + c

    fig, ax = plt.subplots()
    ax.plot(x, y, label=f'{a}x² + {b}x + {c}', color='blue')
    ax.axhline(0, color='black', linewidth=2)
    ax.axvline(0, color='black', linewidth=2)
    ax.set_title('Gráfico de uma função de segundo grau')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)
    ax.grid(True)
    ax.legend()

    if vertice:
        ax.plot(x_vertice, y_vertice, 'ro', label='Vértice')
    
    return fig

# Configurações do Streamlit
st.title("Função de Segundo Grau")

st.sidebar.header("Parâmetros da Função")
a = st.sidebar.number_input("Coeficiente a", value=1, step=1, format="%d")
b = st.sidebar.number_input("Coeficiente b", value=0, step=1, format="%d")
c = st.sidebar.number_input("Coeficiente c", value=0, step=1, format="%d")

if a == 0:
    st.error("O coeficiente 'a' não pode ser zero.")
else:
    fig = plot_funcao_segundo_grau(a, b, c)
    st.pyplot(fig)
