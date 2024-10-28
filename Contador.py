import streamlit as st
import json

# Função para carregar o contador de um arquivo JSON
def carregar_contador():
    try:
        with open("contador.json", "r") as f:
            dados = json.load(f)
            return dados["contador"]
    except FileNotFoundError:
        return 0

# Função para salvar o contador no arquivo JSON
def salvar_contador(contador):
    with open("contador.json", "w") as f:
        json.dump({"contador": contador}, f)

# Carrega e incrementa o contador
contador = carregar_contador()
contador += 1
salvar_contador(contador)

# Exibe o número de acessos
st.title("Contador de Acessos Global")
st.write(f"Esta página foi acessada {contador} vezes.")
