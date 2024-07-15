'''
Desde este archivo llamaremos a las funciones necesarias para realizar el EDA y la limpieza del csv original.
Esas funciones están en el archivo Soporte_Limpieza.
'''
#%%
import pandas as pd
import os 
import sys

#%%
os.getcwd()

#%%
sys.path.append("../")

#%%
from src import Soporte_Limpieza as sp

#%%
#0. Traemos el csv original
url= "https://raw.githubusercontent.com/RachelCaste/project-da-promo-H-modulo-4-team-2/main/src/finanzas-hotel-bookings.csv"
df=sp.read_csv(url)


#%%
#1. Llamamos ala función para el EDA
sp.exploratory_analysis(df)

#%%
#0. Llamamos a la función para calcular porcentaje de nulos
sp.calcular_porcentaje_nulos(df)

#%%
#1. Llamamos a la función para renombrar la columna Unnamed
sp.renombrar_columna(df, 'Unnamed: 0', 'reservation_id')

#%%
#2. Definimos la lista que contiene filas nulas que queremos eliminar
lista_eliminar=['lead_time', 'hotel']
#Llamamos a la función para eliminar filas nulas
sp.eliminar_filas_nulas(df, lista_eliminar)

#%%
#3. Llamamos a la función para corregir datos de la columna arrival_date_month
sp.correccion_meses(df, 'arrival_date_month')

#%%
#4. Llamamos a la función para sustituir 1 y 0 por True y False
sp.float_a_string(df, 'is_repeated_guest')

#%%
#5. Llamamos a la función para transformar el tipo de dato y corregir las fechas de reservation_status_date
sp.convertir_a_fecha(df, 'reservation_status_date')

#%%
#6. Llamamos a la función para sustituir nulos de reserved_room_type con los valores de assigned_room_type
sp.fill_reserved_rooms(df, 'reserved_room_type')

#%%
#7. Llamamos a la función para sustituir nulos de arrival_date_year con el año de reservation_status_date.
sp.fill_arrival_year(df,'arrival_date_year', 'reservation_status_date')

#%%
#8. Llamamos a la función para corregir valores negativos en la columna adr
sp.valores_negativos(df, 'adr')

#%%
#9. Creamos lista Undefined
lista_undefined=['country', 'market_segment', 'distribution_channel', 'is_repeated_guest', 'customer_type']

#Creamos lista de float a int
lista_float_to_int=['lead_time', 'arrival_date_year', 'arrival_date_week_number', 'arrival_date_day_of_month', 'stays_in_weekend_nights', 'stays_in_week_nights', 'adults', 'children', 'babies', 'previous_cancellations', 'previous_bookings_not_canceled', 'booking_changes', 'agent', 'company', 'days_in_waiting_list', 'adr', 'required_car_parking_spaces', 'total_of_special_requests']

#Llamamos a la función para asignar Undefined a los nulos restantes de las columna categóricas
sp.nulos_undefined(df, lista_undefined)

#%%
#10 Llamamos a la función para convertir todas las columnas numéricas a integer (la mayoría son erróneamente float) y asignamos NaN a los nulos restantes
sp.float_to_int(df, lista_float_to_int)

#%%
#11. Llamamos a la función para sustituir nulos de reservation_status_date por 1111-11-11
sp.nulos_fecha(df, 'reservation_status_date')

#%%
#12. Creamos lista de columnas a eliminar
lista_columnas_eliminar=['0', 'company']

#Llamamos a la función para eliminar columnas innecesarias
sp.eliminar_columnas(df, lista_columnas_eliminar)

#%%
#Exportamos csv limpio
df.to_csv('finanzas-hotel-bookings-clean.csv')

#%%