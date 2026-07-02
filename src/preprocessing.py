"""
Funciones de limpieza y transformación.
"""
import pandas as pd

#LIMPIAR BRECHA
def clean_wage_data(df):

    """
    Convierte el dataset original
    en la tabla utilizada
    para el análisis.
    """

    df = df.copy()

    # -----------------------------
    # Limpiar nombres
    # -----------------------------

    df.columns = (

        df.columns
            .str.strip()
            .str.lower()
            .str.replace(" ", "_")

    )

    # -----------------------------
    # Crear tabla dinámica
    # -----------------------------

    brecha = df.pivot_table(

        index="time",

        columns="sex",

        values="monthly_wage",

        aggfunc="mean"

    )

    # -----------------------------
    # Brecha
    # -----------------------------

    brecha["Brecha_%"] = (

        (brecha["Hombre"] - brecha["Mujer"])

        / brecha["Hombre"]

    ) * 100

    # -----------------------------
    # Fecha
    # -----------------------------

    brecha = brecha.reset_index()

    brecha["Fecha"] = pd.to_datetime(

        brecha["time"],

        unit="ms"

    )

    brecha["Año"] = brecha["Fecha"].dt.year

    brecha = brecha.set_index(

        "Año"

    )

    return brecha

# PROMEDIO ANUAL
def create_annual_salary(
    brecha: pd.DataFrame
) -> pd.DataFrame:

    salario_anual = (

    brecha

    .groupby(level=0)

    [["Hombre","Mujer"]]

    .mean()

)
    return salario_anual


# LIMPIEZA DEL INPC
def clean_inpc(
    inpc: pd.DataFrame
) -> pd.Series:

    inpc = inpc.copy()

    inpc.columns = [
        "fecha",
        "inpc",
        "inpp",
        "subyacente"
    ]

    inpc = inpc.iloc[2:].copy()

    meses = {

        "Ene": "Jan",
        "Feb": "Feb",
        "Mar": "Mar",
        "Abr": "Apr",
        "May": "May",
        "Jun": "Jun",
        "Jul": "Jul",
        "Ago": "Aug",
        "Sep": "Sep",
        "Oct": "Oct",
        "Nov": "Nov",
        "Dic": "Dec"

    }

    inpc["fecha"] = (
        inpc["fecha"]
        .replace(
            meses,
            regex=True
        )
    )

    inpc["fecha"] = pd.to_datetime(
        inpc["fecha"],
        format="%b %Y"
    )

    inpc["inpc"] = pd.to_numeric(
        inpc["inpc"]
    )

    inpc["Año"] = (
        inpc["fecha"]
        .dt.year
    )

    inpc_limpio = (
        inpc.groupby("Año")["inpc"].mean()
    )

    return inpc_limpio


# DATASET FINAL
def build_comparison(
    salario_anual: pd.DataFrame,
    inpc: pd.Series
) -> pd.DataFrame:

    comparacion = salario_anual.merge(
        inpc,
        left_index=True,
        right_index=True
    )

    comparacion["brecha_abs"] = (comparacion["Hombre"] - comparacion["Mujer"])

    comparacion["hombre_real"] = (comparacion["Hombre"]/
        (comparacion["inpc"] / 100)
    )

    comparacion["mujer_real"] = (comparacion["Mujer"] / 
        (comparacion["inpc"] / 100)
    )

    comparacion["brecha_real"] = (
        comparacion["hombre_real"] - comparacion["mujer_real"]
    )

    comparacion["ratio"] = (comparacion["Mujer"] / comparacion["Hombre"]
    )

    return comparacion