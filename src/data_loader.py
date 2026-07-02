"""
Funciones para cargar los conjuntos de datos utilizados
en el proyecto de Brecha Salarial.
"""

import pandas as pd
import streamlit as st

# SALARIOS
@st.cache_data
def load_wage_data(
    path: str = "data/salario_genero.csv"
) -> pd.DataFrame:
    df = pd.read_csv(path)

    return df

# INPC
@st.cache_data
def load_inpc_data(
    path: str = "data/evolucion_inpc.csv"
) -> pd.DataFrame:
    df = pd.read_csv(
        path,
        encoding="latin1",
        skiprows=4
    )
    return df