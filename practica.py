#muestra un gráfico
#de uso de m3 y de número de clientes
import pandas as pd
import matplotlib.pyplot as plt
def mostrar_grafico():
    datos = pd.read_csv('C:\\Users\\Tecnicos\\Desktop\\Daniel\\Programacion\\agua.csv')
    df = datos[['Ús','m3_registrats','núm_clients']]



