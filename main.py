import numpy as np
from sklearn.tree import DecisionTreeClassifier
# TEMPO DE USO DE UM PRODUTO x RECLAMAÇÃO
# y = f(x)


X = np.array([
    [3,0],
    [2,0],
    [3,3],
    [4,1],
    [5,1],     
])


#investimento de marketing


# import numpy  as np
# from sklearn.linear_model import LinearRegression
# # investimento em mkt 1mil
# X = np.array([[1],[2],[4],[5],[3]])
# # vendas 
# y =  np.array([2,8,4,6,5])

# modelo = LinearRegression()


# modelo.fit(X, y)


# print(modelo.predict([[6]]))


import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

st.header("Previsão de Vendas")

# Dados: [Investimento em Marketing] -> Faturamento
dados_vendas = pd.DataFrame({
    'investimento': [100, 200, 300, 400, 500, 600],
    'faturamento': [1200, 2500, 3200, 4800, 5100, 6300]
})

st.scatter_chart(dados_vendas, x = 'investimento', y= 'faturamento')
modelo = LinearRegression()
modelo.fit(dados_vendas[['investimento']], dados_vendas['faturamento'])
imvestimento = st.number_input('seu investimento')
previsaofaturamento = modelo.predict([[imvestimento]])
if st.button('prever'): 
    st.metric('seu faturamento é', previsaofaturamento)
