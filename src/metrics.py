"""
Funciones para calcular indicadores del dashboard.
"""
import pandas as pd

# KPIs POR AÑO
def year_metrics(
    comparacion: pd.DataFrame,
    year: int
) -> dict:

    fila = comparacion.loc[year]

    return {

        "male_salary":
            fila["Hombre"],

        "female_salary":
            fila["Mujer"],

        "real_male":
            fila["hombre_real"],

        "real_female":
            fila["mujer_real"],

        "gap":

            fila["brecha_abs"],

        "real_gap":

            fila["brecha_real"],

        "ratio":

            fila["ratio"],

        "inpc":

            fila["inpc"]

    }


# MEJOR AÑO
def best_year(
    comparacion: pd.DataFrame
):

    return comparacion["ratio"].idxmax()

# PEOR AÑO
def worst_year(
    comparacion: pd.DataFrame
):

    return comparacion["ratio"].idxmin()

# MAYOR BRECHA
def largest_gap(
    comparacion: pd.DataFrame
):

    return comparacion["brecha_abs"].max()


# MENOR BRECHA
def smallest_gap(
    comparacion: pd.DataFrame
):

    return comparacion["brecha_abs"].min()

# PROMEDIOS
def averages(
    comparacion: pd.DataFrame
):

    return {

        "male":

        comparacion["Hombre"].mean(),

        "female":

        comparacion["Mujer"].mean(),

        "ratio":

        comparacion["ratio"].mean(),

        "gap":

        comparacion["brecha_abs"].mean()

    }


# CRECIMIENTO
def growth(
    comparacion: pd.DataFrame,
    column: str
):

    inicio = comparacion[column].iloc[0]

    fin = comparacion[column].iloc[-1]

    crecimiento = (
        (
            fin
            - inicio
        )
        /
        inicio
    ) * 100

    return crecimiento