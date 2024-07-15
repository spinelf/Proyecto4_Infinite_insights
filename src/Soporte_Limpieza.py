'''
En este archivo se encuentran todas las funciones necesarias para realizar la limpieza del csv original.
Llamaremos a cada función desde el archivo Main_Limpieza.
'''

'''0. Importación de librerías y datos.'''
#%%
#Importamos librerías
import pandas as pd
import numpy as np
pd.set_option('display.max_columns', None)

#%%
#Función para leer el csv original
def read_csv(link):
    df=pd.read_csv(link, index_col=0)
    return df

#%%
'''1. EDA'''
#%%
#Creamos función para EDA
def exploratory_analysis(df):

    #Vemos la forma del dataframe
    print(f'There are {df.shape[0]} rows and {df.shape[1]} columnas in the dataframe.')
    print('\n--------------------------------\n')

    #Vemos la información general
    print('General info:\n')
    df.info()
    print('\n--------------------------------\n')

    #Sacamos un df con la cantidad de nulos y su %
    df_null=pd.DataFrame({'Null': df.isnull().sum(),
                          '% null': (df.isnull().mean()*100).round(2)})
    print('Total nulls:')
    display(df_null)
    print('\n--------------------------------\n')

    #Sacamos los duplicados
    duplicates=df.duplicated().sum()
    if duplicates > 0:
        print(f'There are a total of {duplicates} duplicates in the DataFrame.')
        print('\n--------------------------------\n')
    else:
        print('There are no duplicates in the DataFrame.')
        print('\n--------------------------------\n')


    #Sacamos las estadísticas de las columnas categóricas y de las columnas numéricas
    categorical_columns=df.select_dtypes(include='O').columns
    if len(categorical_columns) == 0:
        print(f'There are no categorical columns in the DataFrame.')
        print('\n--------------------------------\n')

    else:
        print("Categorical columns' statistics:")
        display(df.describe(include='O').T)
        print('\n--------------------------------\n')

    print("Numerical columns' statistics:")
    display(df.describe().T)
    print('\n--------------------------------\n')

    #Sacamos la cantidad de valores únicos diferentes de cada columna
    for i in df.columns:
        different_unique_values=df[i].nunique()
        print(f'Total different unique values per column {i.upper()}: {different_unique_values}')

'''
2. Limpieza.

Acciones:

1. Renombramos la columna Unnamed.

2. Eliminamos filas nulas (aquellas filas con nulos en la mayorías de sus celdas: lead_time y hotel).

3. Corregimos datos de la columna arrival_date_month.

4. Sustituimos 1 y 0 por True y False en la columna is_repeated_guest.

5. Transformamos el tipo de dato y corregimos las fechas de reservation_status_date.

6. Sustituimos nulos de reserved_room_type con los valores de assigned_room_type.

7. Sustituimos nulos de arrival_date_year con el año de reservation_status_date.

8. Corregimos valor negativo en la columna adr.

9. Asignamos Undefined a los nulos restantes de las columna categóricas.

10. Convertimos todas las columnas numéricas a integer (la mayoría son erróneamente float) y asignamos 99999 a los nulos restantes.

11. Sustituimos nulos de reservation_status_date por 1111-11-11.

12. Eliminamos columnas innecesarias (0 y company).
'''
#%%
#0. Función para calcular nulos
def calcular_porcentaje_nulos(df):
    """
    Calcula el porcentaje de valores nulos en un DataFrame y muestra las columnas con más de cero nulos.
    
    Args:
        df (pd.DataFrame): El DataFrame de entrada.
    
    Returns:
        pd.DataFrame: Un DataFrame con las columnas y sus porcentajes de valores nulos.
    """
    porcentaje_null = (df.isnull().sum() / df.shape[0]) * 100
    nulos_dataf = pd.DataFrame(porcentaje_null.round(2), columns=["Nulos_Porcentaje"])
    return nulos_dataf[nulos_dataf["Nulos_Porcentaje"] > 0]

#%%
#1. Función para renombar la columna Unnamed
def renombrar_columna(df, old_name, new_name):
    df.rename(columns={old_name: new_name}, inplace=True)

#%%
#2. Función para eliminar filas nulas (aquellas filas con nulos en la mayorías de sus celdas).
def eliminar_filas_nulas(df, columnas):
    df.dropna(subset=columnas, inplace=True)

#%%
#3. Función para corregir datos de la columna arrival_date_month
def correccion_meses(df, columna):
    """
    Creamos un diccionario para mapear la columna arrival_date_month y corregir los presentes y futuros errores
    """
    meses={'1':'January', '2':'February', '3':'March', '4':'April', '5':'May', '6':'June', '7':'July', '8':'August', '9':'September', '10':'Ocober', '11':'November', '12':'December'}
    df[columna]=df[columna].map(meses).fillna(df[columna]) #.fillna(df[columna]) asegura que si en la columna había un valor que no está en el diccionario (por ejemplo, 13) se conserve y no se sustituya por NaN.

#%%
#4. Función para sustituir 1 y 0 por True y False en la columna is_repeated_guest
def float_a_string(df, columna):
    df[columna]=df[columna].astype(str).str.split('.').str[0]
    df[columna]=df[columna].replace('1', 'True').replace('0', 'False')
    df[columna]=df[columna].replace('nan', np.nan) #para que no sea la palabra 'nan', sino nulo

#%%
#5. Función para transformar el tipo de dato y corregir las fechas de reservation_status_date
def convertir_a_fecha(df, columna):
    #Convierte la columna a datetime, y los errores a NaT
    df[columna]=pd.to_datetime(df[columna], errors='coerce')
    #Extrae sólo la parte de la fecha
    df[columna]=df[columna].dt.date

#%%
#6. Función para sustituir nulos de reserved_room_type con los valores de assigned_room_type
def fill_reserved_rooms(df, columna):
    df[columna]=df[columna].fillna(df['assigned_room_type'])

#%%
#7. Función para sustituir nulos de arrival_date_year con el año de reservation_status_date.
def fill_arrival_year(df, target_col, date_col):
    #Extraemos el año de la columna reservation_status_date y sustituimos los nulos de target_col con esos años
    df[target_col]=df[target_col].fillna(pd.to_datetime(df[date_col]).dt.year)

#%%
#8. Función para corregir valores negativos en la columna adr
def valores_negativos(df, columna):
    df[columna]=abs(df[columna])

#%%
#9. Función para asignar Undefined a los nulos restantes de las columna categóricas
def nulos_undefined(df, lista_columnas):
    for i in lista_columnas:
        df[i]=df[i].fillna('Undefined')

#%%
#10. Función para convertir todas las columnas numéricas a integer (la mayoría son erróneamente float) y asignamos NaN a los nulos restantes
def float_to_int(df, lista_columnas):
    for i in lista_columnas:
        #Dividimos por el '.' y nos quedamos con la primera parte
        df[i]=df[i].astype(str).str.split('.').str[0]

        #Reemplazamos 'nan' con NaN
        df[i]=df[i].replace('nan', '99999')

        #Convertimos a Int64
        df[i]=pd.to_numeric(df[i]).astype('Int64')

#%%
#11. Función para sustituir nulos de reservation_status_date por 1111-11-11
def nulos_fecha(df, columna):
    df[columna] = df[columna].fillna(pd.Timestamp('1111-11-11'))

#%%
#12. Función para eliminar columnas innecesarias
def eliminar_columnas(df, lista_columnas):
    df.drop(columns=lista_columnas, inplace=True)

#%%
