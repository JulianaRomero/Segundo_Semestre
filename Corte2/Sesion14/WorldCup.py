#1. Conocer el numero de copas mundo que un país ha ganado
#2. Conocer el numero de subcampeonatos que un país ha ganado
#3. Conocer el numero de participaciones de un equipo al mundial
#4. Conocer el numero de copas mundiales jugadas hasta la fecha
#5. Conocer el número de asistentes a las copas mundiales
#6. Conocer el número de finales disputadas por penales
#7. Conocer el número de goles a favor de los equipos en los mundiales
#8. Conocer el número de goles en contra de los equipos en los mundiales
#9. Conocer la diferencia de goles en todas sus presentaciones
#10. Conocer el promedio de goles de un equipo en mundiales
#11. Conocer cuantas veces se han enfrentado 2 equipos en los mundiales\n
#12. Conocer cual es el mundial con más penales
#13. Conocer cual es el mundial con mayor número de goles

def campeones(listado):
    campeon={}
    for partidos in listado:
        if partidos[12]=='Final': 
            if (partidos[2]>partidos[4]) or (partidos[3]>partidos[5]):
                if partidos[0] not in campeon:
                    campeon[partidos[0]]= [partidos[16]]
                else:
                    year=campeon[partidos[0]]
                    year.append(partidos[16])
                    campeon[partidos[0]]=year
            else:
                if partidos[1] not in campeon:
                    campeon[partidos[1]]= [partidos[16]]
                else:
                    year=campeon[partidos[1]]
                    year.append(partidos[16])
                    campeon[partidos[1]]=year
    
    campeon=dict(sorted(campeon.items()))
    for equipo, year in (campeon.items()):
        print(f'{equipo}: {year}')
    
def subcampeones(listado):
    subcampeon={}
    for partidos in listado:
        if partidos[12]=='Final': 
            if (partidos[2]>partidos[4]) or (partidos[3]>partidos[5]):
                if partidos[1] not in subcampeon:
                    subcampeon[partidos[1]]= [partidos[16]]
                else:
                    year=subcampeon[partidos[1]]
                    year.append(partidos[16])
                    subcampeon[partidos[1]]=year
            else:
                if partidos[0] not in subcampeon:
                    subcampeon[partidos[0]]= [partidos[16]]
                else:
                    year=subcampeon[partidos[0]]
                    year.append(partidos[16])
                    subcampeon[partidos[0]]=year
    
    subcampeon=dict(sorted(subcampeon.items()))
    for equipo, year in (subcampeon.items()):
        print(f'{equipo}: {year}')

def main():
    listado=lectura()
    print(listado[0])
    subcampeones(listado)

if __name__=="__main__":
    main()