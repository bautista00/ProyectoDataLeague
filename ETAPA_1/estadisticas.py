import random
import partidos

def calcular_tabla_posiciones(resultados, equipos):
    """Calcula la tabla de posiciones para equipos habilitados."""
    # equipos:
    # - equipo[1] = abreviatura
    # - equipo[2] = estado ('H' = habilitado)
    equipos_habilitados = []
    for equipo in equipos:
        if equipo[2] == 'H':  
            equipos_habilitados.append(equipo)
    
    if len(equipos_habilitados) == 0:
        return []
        
    # tabla: lista de filas (una por equipo)
    # 0: abrev | 1: PJ | 2: PG | 3: PE | 4: PP | 5: GF | 6: GC | 7: DG | 8: Pts
    tabla = []
    for equipo in equipos_habilitados:
        
        tabla.append([equipo[1], 0, 0, 0, 0, 0, 0, 0, 0])
    

    for i in range(len(equipos_habilitados)):
        for j in range(len(equipos_habilitados)):
            if i != j:  
                resultado = partidos.obtener_resultado_partido(resultados, i, j)
                goles_local = resultado[0]
                goles_visitante = resultado[1]
                
                
                tabla[i][1] += 1  # 1: PJ 
                tabla[i][5] += goles_local  # 5: GF 
                tabla[i][6] += goles_visitante  # 6: GC 
                
                if goles_local > goles_visitante:
                    tabla[i][2] += 1  # 2: PG 
                    tabla[i][8] += 3  # 8: Pts 
                elif goles_local == goles_visitante:
                    tabla[i][3] += 1  # 3: PE 
                    tabla[i][8] += 1  # 8: Pts 
                else:
                    tabla[i][4] += 1  # 4: PP
    
    for fila in tabla:
        fila[7] = fila[5] - fila[6]  # diferencia de goles = goles a favor - goles en contra
    
    tabla_ordenada = ordenar_tabla(tabla)
    
    return tabla_ordenada

def ordenar_tabla(tabla):
    tabla.sort(key=lambda x: x[5], reverse=True)  # 3ª prioridad    goles a favor
    tabla.sort(key=lambda x: x[7], reverse=True)  # 2ª prioridad    diferencia de goles
    tabla.sort(key=lambda x: x[8], reverse=True)  # 1ª prioridad    puntos
    return tabla

def calcular_estadisticas_equipo(resultados, abrev, equipos):
    """Calcula estadísticas de un equipo específico."""
    
    tabla = calcular_tabla_posiciones(resultados, equipos)
    
    for fila in tabla:
        if fila[0] == abrev:
            return fila[1:]  # Retorna las estadísticas del equipo encontrado (sin nombre)
    
    return [0, 0, 0, 0, 0, 0, 0, 0]  # Retorna estadísticas vacías si el equipo no se encuentra

def calcular_ranking_goleadores(resultados, jugadores):
    """Genera el ranking de goleadores ordenado por goles."""
    
    # Estructura jugador: [0]nombre, [1]dorsal, [2]posicion, [3]equipo, [4]estado, [5]tarjetas_amarillas, [6]fechas_suspension, [7]tipo_sancion
    # - jugador[0] = nombre del jugador
    # - jugador[3] = abreviatura del equipo  
    # - jugador[4] = estado ('H' = habilitado, 'S' = suspendido)
    # ranking: lista de filas con formato -> [0] nombre | [1] equipo | [2] goles
    ranking = []
    for jugador in jugadores:
        if jugador[4] == 'H':
            goles = random.randint(0, 10)  # simulación de goles
            ranking.append([jugador[0], jugador[3], goles])
    
    # Ordenar por goles descendente, el signo hace que el jugador con más goles sea el primero
    ranking.sort(key=lambda x: (-x[2], x[0]))
    
    return ranking

def calcular_sanciones_vigentes(jugadores):
    """Retorna una lista de jugadores con sanciones vigentes."""
    sancionados = []
    
    for jugador in jugadores:
        if int(jugador[6]) > 0:  
            sancionados.append([jugador[0], jugador[3], jugador[7], jugador[6]])
    
    return sancionados

def calcular_historial_equipo(resultados, abrev):
    """Genera el historial de partidos de un equipo."""
    historial = []
    
    return historial

def calcular_estadisticas_arbitros(resultados, arbitros):
    """Calcula estadísticas de árbitros."""
    stats = []
    
    for arbitro in arbitros:
        if arbitro[2] == 'A':  
            partidos = random.randint(0, 20)
            tarjetas = random.randint(0, 50)
            if partidos > 0:
                promedio = tarjetas / partidos
            else:
                promedio = 0
            stats.append([arbitro[0], partidos, tarjetas, promedio])
    
    return stats

def aplicar_sorteo_desempate(empatados):
    """Aplica un sorteo para desempatar equipos."""
    
    n = len(empatados)
    for i in range(n - 1, 0, -1):
        j = random.randint(0, i)
        
        temp = empatados[i]
        empatados[i] = empatados[j]
        empatados[j] = temp
    
    return empatados
