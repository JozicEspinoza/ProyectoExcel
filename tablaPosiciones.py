# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 12:54:33 2021

@author: jozic
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
 

def header ():
    print("\n\n")
    print("\x1b[1;33m"+"************************************")
    print("\033[;36m"+ " SISTEMA DE ESTADISTICAS DEPORTIVAS")
    print("\x1b[1;33m"+"************************************")
    print("\x1b[1;36m\n")
    
def matchesStadistic():
    df = pd.read_excel(io = "ejemplo.xlsx", sheet_name="Hoja1")
    plt.title('Partidos Ganados VS Perdidos VS Empatados')
    plt.ylabel("Partidos")
    plt.xlabel("Equipos")
    looseMatch = df['Perdidos']
    wonMatch = df['Ganados']
    drawMatch = df['Empatados']
    groupsNumber = len(looseMatch)
    barIndex = np.arange(groupsNumber)
    barWidth =0.35
    plt.bar(barIndex+ barWidth, looseMatch, width=barWidth, label='Perdidos')
    plt.bar(barIndex + (barWidth*2), wonMatch, width=barWidth, label='Ganados')
    plt.bar(barIndex + (barWidth*3), drawMatch, width=barWidth, label='Empatados')
    plt.xticks(barIndex + barWidth, (df['Equipo']), rotation=90)
    plt.legend(loc='best')
    plt.grid(color='b', linestyle='solid', linewidth=40)
    plt.show()

def goalsStadistic():
    df = pd.read_excel(io = "ejemplo.xlsx", sheet_name="Hoja1")
    plt.title('Goles anotados VS Goles recibidos')
    plt.ylabel("Goles")
    plt.xlabel("Equipos")
    correctGoal = df['Gf']
    wrongGoal = df['Gc']
    groupsNumber = len(correctGoal)
    barIndex = np.arange(groupsNumber)
    barWidth =0.35
    plt.bar(barIndex+ barWidth, correctGoal, width=barWidth, label='Goles a favor')
    plt.bar(barIndex + (barWidth*2), wrongGoal, width=barWidth, label='Goles en contra')
    plt.xticks(barIndex + barWidth, (df['Equipo']), rotation=90)
    plt.legend(loc='best')
    plt.grid(color='b', linestyle='solid', linewidth=40)
    plt.show()

def optionMenu():
    customerSelection = 0
    while customerSelection == 0 : 
        header()
        option=str(input("Seleccione la opcion deseada:\n1) Tabla de posiciones\n2) Tabla de goleo\n3) Graficas\n4) Salir\nOpcion:  "))
        if option == "1":
            header ()
            df = pd.read_excel(io = "ejemplo.xlsx", sheet_name="Hoja1")
            print("\x1b[1;35m")
            print(df.set_index('Posicion'))
        elif option == "2":
            header ()
            df = pd.read_excel(io = "ejemplo.xlsx", sheet_name="Hoja2")
            print("\x1b[1;35m")
            print(df.set_index('Posicion'))
        elif option == "3":
            stadistic=0
            while stadistic == 0:
                header ()
                StadisticOption=str(input("Seleccione la opcion deseada:\n1) Comparacion de posiciones\n2) Comparacion de goleo\n3) Salir\nOpcion:  "))
                if StadisticOption == "1":
                    header ()
                    matchesStadistic()
                    stadistic=1
                elif StadisticOption == "2":
                    header ()
                    goalsStadistic()
                    stadistic=1
                else:
                    print("Opcion incorrecta, intente con otra opcion")
        else:
            print("Opcion incorrecta, ingrese otra")
            

def main():
    optionMenu()
    
if __name__ == '__main__':
    main()