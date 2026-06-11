README 

Hipótesis inicial: 
la brecha salarial entre hombres y mujeres vs el costo de vida hombres y mujeres. - Quiero entenderlo con datos porque así podré comprender cuál es la diferencia percentual, visibilizar el problema y buscar soluciones. ¿Qué productos son más costosos para mujeres que hombres? ¿Qué los hace diferente? ¿Cómo ha crecido o disminuido la brecha salarial a lo largo de los años? ¿En qué áreas existe mayor brecha salarial y en qué porcentaje difiere? ¿Qué estados tienen menor brecha salarial?


Código Python:

import pandas as pd
df_genero = pd.read_csv("proyecto_brecha_salarial/data/salario_genero.csv")
df_inpc = pd.read_csv("proyecto_brecha_salarial/data/evolucion_inpc.csv",
                     encoding="latin1")
df_sector = pd.read_csv("proyecto_brecha_salarial/data/fuerzalaboral_ocupacion_salariopromedio.csv")
df_gini = pd.read_csv("proyecto_brecha_salarial/data/desigualdad_social_gini_mexico.csv")

df_genero.head(), df_genero.info()
df_inpc.head(), df_inpc.info()
df_sector.head, df_sector.info()
df_gini.head(), df_gini.info()


Columnas:

Columnas de df_genero: 9 columnas. 
#   Column        Non-Null Count  Dtype  
---  ------        --------------  -----  
 0   Nation ID     120 non-null    object 
 1   Nation        120 non-null    object 
 2   Quarter ID    120 non-null    int64  
 3   Quarter       120 non-null    object 
 4   Sex ID        120 non-null    int64  
 5   Sex           120 non-null    object 
 6   Monthly Wage  120 non-null    float64
 7   Workforce     120 non-null    int64  
 8   Time          120 non-null    int64  
dtypes: float64(1), int64(4), object(4)
RangeIndex: 120 entries, 0 to 119

Columnas de df_inpc: Columnas 220 entries, I to Unnamed: 219
dtypes: float64(220)
RangeIndex: 14 entries, 0 to 13

Columnas de df_sector: 17 columnas
#   Column                     Non-Null Count  Dtype  
---  ------                     --------------  -----  
 0   Category ID                459 non-null    int64  
 1   Category                   459 non-null    object 
 2   Group ID                   459 non-null    int64  
 3   Group                      459 non-null    object 
 4   Subgroup ID                459 non-null    int64  
 5   Subgroup                   459 non-null    object 
 6   Occupation ID              459 non-null    int64  
 7   Occupation                 459 non-null    object 
 8   Year                       459 non-null    int64  
 9   Quarter ID                 459 non-null    int64  
 10  Quarter                    459 non-null    object 
 11  Workforce                  459 non-null    int64  
 12  Monthly Wage               459 non-null    float64
 13  Monthly Wage Growth        459 non-null    float64
 14  Monthly Wage Growth Value  459 non-null    float64
 15  percentage                 459 non-null    float64
 16  lastPeriod                 459 non-null    float64
dtypes: float64(5), int64(7), object(5)
RangeIndex: 459 entries, 0 to 458

Columnas de df_gini:6 columnas. 
#   Column      Non-Null Count  Dtype  
---  ------      --------------  -----  
 0   Nation ID   32 non-null     object 
 1   Nation      32 non-null     object 
 2   State ID    32 non-null     int64  
 3   State       32 non-null     object 
 4   GINI        32 non-null     float64
 5   Population  32 non-null     int64  
dtypes: float64(1), int64(2), object(3)
RangeIndex: 32 entries, 0 to 31


Cambio de hipótesis: 
¿Cómo evoluciona la brecha salarial nacional ajustada al costo de vida y cómo se relaciona con la desigualdad estructural de los estados?



| Pregunta social                                    | Lo que sí puedes medir                      |
| -------------------------------------------------- | ------------------------------------------- |
| ¿Existe brecha salarial?                           | Salario mujeres vs hombres por año          |
| ¿Está creciendo o bajando?                         | Evolución de esa brecha                     |
| ¿Se come la inflación los salarios de las mujeres? | Salario real (ajustado por INPC)            |
| ¿En qué sectores hay más brecha?                   | `df_sector` por ocupación                   |
| ¿Dónde es más desigual?                            | GINI por estado (como contexto estructural) |


Primero resultados:
Análisis 1: 

📌 Eso significa:

Las mujeres ganan 24.97% menos que los hombres por el mismo mercado laboral.

O dicho más fuerte:

Por cada 100 pesos que gana un hombre, una mujer gana 75 pesos.

Porque:

100
−
24.97
=
75.03
100−24.97=75.03


En México, durante más de una década,
las mujeres han ganado entre 15% y 25% menos que los hombres,
incluso cuando la economía crece.