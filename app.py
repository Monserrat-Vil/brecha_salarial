"""
Main Dashboard
Brecha Salarial por Género en México
"""

import streamlit as st

from src.data_loader import *

from src.preprocessing import *

from src.metrics import *

from src.plots import *

# CONFIGURACION DE PAGINA

st.set_page_config(

    page_title="Brecha Salarial",

    page_icon="📊",

    layout="wide",

    initial_sidebar_state="expanded"

)

# CARGA DE DATOS

wage = load_wage_data()

inpc = load_inpc_data()

# PRE-PROCESO

brecha = clean_wage_data(wage)

salario_anual = create_annual_salary(

    brecha

)

inpc = clean_inpc(

    inpc

)

comparacion = build_comparison(

    salario_anual,

    inpc

)

# SIDEBAR

st.sidebar.image(

    "https://streamlit.io/images/brand/streamlit-mark-color.png",

    width=120

)

st.sidebar.title(

    "Controles de Dashboard"

)

salary_type = st.sidebar.radio(

    "Tipo de Salario",

    [

        "Nominal",

        "Real"

    ]

)

selected_year = st.sidebar.slider(

    "Año",

    int(comparacion.index.min()),

    int(comparacion.index.max()),

    int(comparacion.index.max())

)

st.sidebar.divider()

st.sidebar.markdown(

"""
### About

Interactive dashboard built with

- Streamlit

- Plotly

- Pandas

- Python

"""
)

# FILTROS

filtered = comparacion.loc[

    comparacion.index <= selected_year

]

# ENCABEZADO

st.title(

    "📊 Brecha Salarial por Género en México"

)

st.caption(

    "2010–2025"

)

st.divider()

# KPIs

metric = year_metrics(

    comparacion,

    selected_year

)

col1, col2, col3, col4 = st.columns(4)

with col1:

    st.plotly_chart(

        indicator(

            "Men Salary",

            metric["male_salary"],

            " MXN"

        ),

        use_container_width=True

    )

with col2:

    st.plotly_chart(

        indicator(

            "Women Salary",

            metric["female_salary"],

            " MXN"

        ),

        use_container_width=True

    )

with col3:

    st.plotly_chart(

        indicator(

            "Gap",

            metric["gap"],

            " MXN"

        ),

        use_container_width=True

    )

with col4:

    st.plotly_chart(

        indicator(

            "Ratio",

            metric["ratio"]*100,

            "%"

        ),

        use_container_width=True

    )

st.divider()

# TABS

tab1, tab2, tab3, tab4, tab5 = st.tabs(

    [

        "Overview",

        "Real Salary",

        "Inflation",

        "Patterns",

        "Dataset"

    ]

)


# OVERVIEW


with tab1:

    st.subheader(

        "Nominal Salary"

    )

    st.plotly_chart(

        nominal_salary_plot(

            filtered

        ),

        use_container_width=True

    )

    st.subheader(

        "Gap"

    )

    st.plotly_chart(

        gap_plot(

            filtered

        ),

        use_container_width=True

    )


# REAL


with tab2:

    st.subheader(

        "Real Salary"

    )

    st.plotly_chart(

        real_salary_plot(

            filtered

        ),

        use_container_width=True

    )

    st.subheader(

        "Ratio"

    )

    st.plotly_chart(

        ratio_plot(

            filtered

        ),

        use_container_width=True

    )


# INPC


with tab3:

    st.subheader(

        "Salary vs INPC"

    )

    st.plotly_chart(

        salary_vs_inpc(

            filtered

        ),

        use_container_width=True

    )


# PATRONES


with tab4:

    st.subheader(

        "Correlation"

    )

    st.plotly_chart(

        correlation_heatmap(

            filtered

        ),

        use_container_width=True

    )

    st.subheader(

        "Scatter Matrix"

    )

    st.plotly_chart(

        scatter_matrix(

            filtered

        ),

        use_container_width=True

    )


# DATASET


with tab5:

    st.subheader(

        "Processed Dataset"

    )

    st.dataframe(

        filtered,

        use_container_width=True

    )

    csv = filtered.to_csv().encode()

    st.download_button(

        "📥 Download CSV",

        csv,

        file_name="gender_wage_gap.csv",

        mime="text/csv"

    )

st.divider()

st.caption(

    "Made using Python + Streamlit"

)