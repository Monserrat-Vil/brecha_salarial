"""
Todas las visualizaciones del dashboard.
"""

import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots


# PALETA DE COLORES

COLORS = {

    "male": "#2563EB",
    "female": "#C026D3",

    "gap": "#EF4444",

    "real": "#059669",

    "background": "#F8FAFC"

}

# PLANTILLA

def apply_layout(fig, title):

    fig.update_layout(

        title=dict(

            text=title,

            x=.5,

            xanchor="center"

        ),

        template="plotly_white",

        hovermode="x unified",

        legend_title="",

        height=500,

        margin=dict(

            l=30,

            r=30,

            t=70,

            b=30

        )

    )

    return fig


# SALARIOS NOMINALES 
def nominal_salary_plot(df):

    fig = go.Figure()

    fig.add_trace(

        go.Scatter(

            x=df.index,

            y=df["Hombre"],

            mode="lines+markers",

            name="Men",

            line=dict(

                color=COLORS["male"],

                width=4

            )

        )

    )

    fig.add_trace(

        go.Scatter(

            x=df.index,

            y=df["Mujer"],

            mode="lines+markers",

            name="Women",

            line=dict(

                color=COLORS["female"],

                width=4

            )

        )

    )

    fig.update_yaxes(

        title="Monthly wage"

    )

    fig.update_xaxes(

        title="Year"

    )

    return apply_layout(

        fig,

        "Average Nominal Salary"

    )


# SALARIO REAL

def real_salary_plot(df):

    fig = go.Figure()

    fig.add_trace(

        go.Scatter(

            x=df.index,

            y=df["hombre_real"],

            mode="lines+markers",

            name="Men",

            line=dict(

                color=COLORS["male"],

                width=4

            )

        )

    )

    fig.add_trace(

        go.Scatter(

            x=df.index,

            y=df["mujer_real"],

            mode="lines+markers",

            name="Women",

            line=dict(

                color=COLORS["female"],

                width=4

            )

        )

    )

    fig.update_yaxes(

        title="Real Salary"

    )

    fig.update_xaxes(

        title="Year"

    )

    return apply_layout(

        fig,

        "Real Salary (INPC Adjusted)"

    )


# BRECHA ABSOLUTA 
def gap_plot(df):

    fig = px.area(

        df,

        x=df.index,

        y="brecha_abs",

        color_discrete_sequence=[

            COLORS["gap"]

        ]

    )

    fig.update_yaxes(

        title="MXN"

    )

    return apply_layout(

        fig,

        "Absolute Wage Gap"

    )


# RATIO

def ratio_plot(df):

    fig = px.line(

        df,

        x=df.index,

        y="ratio",

        markers=True

    )

    fig.update_traces(

        line_color=COLORS["real"],

        line_width=4

    )

    fig.update_yaxes(

        tickformat=".0%"

    )

    return apply_layout(

        fig,

        "Women / Men Salary Ratio"

    )


# INPC

def inpc_plot(df):

    fig = px.bar(

        df,

        x=df.index,

        y="inpc",

        color="inpc",

        color_continuous_scale="Viridis"

    )

    return apply_layout(

        fig,

        "Average INPC"

    )


# CORRELACION

def correlation_heatmap(df):

    corr = df.corr(

        numeric_only=True

    )

    fig = px.imshow(

        corr,

        text_auto=".2f",

        aspect="auto",

        color_continuous_scale="RdBu"

    )

    return apply_layout(

        fig,

        "Correlation Matrix"

    )


# MATRIZ DE DISPERSION

def scatter_matrix(df):

    fig = px.scatter_matrix(

        df,

        dimensions=[

            "Hombre",

            "Mujer",

            "hombre_real",

            "mujer_real",

            "inpc"

        ],

        color="ratio",

        color_continuous_scale="Viridis"

    )

    fig.update_traces(

        diagonal_visible=False

    )

    fig.update_layout(

        height=900

    )

    return fig


# KPI TARJETA

def indicator(title, value, suffix=""):

    fig = go.Figure(

        go.Indicator(

            mode="number",

            value=value,

            number={

                "suffix": suffix

            },

            title={

                "text": title

            }

        )

    )

    fig.update_layout(

        height=180,

        margin=dict(

            l=15,

            r=15,

            t=45,

            b=15

        )

    )

    return fig


# 2 ejes

def salary_vs_inpc(df):

    fig = make_subplots(

        specs=[[

            {

                "secondary_y": True

            }

        ]]

    )

    fig.add_trace(

        go.Scatter(

            x=df.index,

            y=df["Hombre"],

            name="Men",

            line=dict(

                color=COLORS["male"]

            )

        ),

        secondary_y=False

    )

    fig.add_trace(

        go.Scatter(

            x=df.index,

            y=df["Mujer"],

            name="Women",

            line=dict(

                color=COLORS["female"]

            )

        ),

        secondary_y=False

    )

    fig.add_trace(

        go.Bar(

            x=df.index,

            y=df["inpc"],

            name="INPC",

            opacity=.30

        ),

        secondary_y=True

    )

    fig.update_yaxes(

        title_text="Salary",

        secondary_y=False

    )

    fig.update_yaxes(

        title_text="INPC",

        secondary_y=True

    )

    return apply_layout(

        fig,

        "Salary vs INPC"

    )


# DESCARGAR IMAGEN

def export_png(fig, filename):

    fig.write_image(

        filename,

        scale=3

    )