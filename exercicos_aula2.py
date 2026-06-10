# calculadora


import streamlit as st


st.title('Calculadora')


numero1 = st.number_input('numero ') 
numero2 = st.number_input('numero ', step=0.1)


if st.button('RESULTADO'):
    soma = numero1 +  numero2
    st.success(soma)


# ----------------------------------------


# calculadora de imc



st.title('Calculo do imc')


peso = st.number_input('PESO')
altura = st.number_input('Altura')


if st.button('Calcular IMC'):
    calculo = round(peso / (altura ** 2), 2)
    st.success(calculo)


#-----------------------------

st.title('tabuada')
number = st.number_input('escola a tabuada')
if st.button('calcular'):
    st.write("0 x ", number, ' = ', number * 0)
    st.write("1 x ", number, ' = ', number * 1)
    st.write("2 x ", number, ' = ', number * 2)
    st.write("3 x ", number, ' = ', number * 3)
    st.write("4 x ", number, ' = ', number * 4)
    st.write("5 x ", number, ' = ', number * 5)
    st.write("6 x ", number, ' = ', number * 6)
    st.write("7 x ", number, ' = ', number * 7)
    st.write("8 x ", number, ' = ', number * 8)
    st.write("9 x ", number, ' = ', number * 9)
    st.write("10 x ", number, ' = ', number * 10)
