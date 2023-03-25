# ... LIBRERIAS PRINCIPALES ...
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# ... CARGAR EL ARCHIVO CON LOS DATOS ...
df = pd.read_csv("C:/Users/Facu/Documents/Python/Proyectos/PrecioCasas/train.csv")

# ... MOSTRAR LAS PRIMERAS FILAS ...
print(df.head())

# ... INFORMACION GENERAL ...
print(df.describe())

# ... MOSTRAR EL NUMERO DE FILAS Y COLUMNAS ...
print(df.shape)

# ... MOSTRAR EL TIPO DE VARIABLE ...
print(df.dtypes)

# ... VALORES DE LA VIABLE CATEGORIA ...
print(df['SaleCondition'].value_counts())

# ... GRAFICA EL PROMEDIO DE PRECIO DE VENTA ...
print(df['SalePrice'].hist())

# ... GRAFICA VARIABLES NUMERICAS ...
print(df.hist(bins=50, figsize=(20,15)))






