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

def calcular_ranking_goleadores(resultados, jugadores, eventos_partidos):
    """Genera el ranking de goleadores ordenado."""
    
    # Estructura jugador: [0]nombre, [1]dorsal, [2]posicion, [3]equipo, [4]estado, [5]tarjetas_amarillas, [6]fechas_suspension, [7]tipo_sancion
    # - jugador[0] = nombre del jugador
    # - jugador[1] = dorsal del jugador
    # - jugador[3] = abreviatura del equipo  
    # - jugador[4] = estado ('H' = habilitado, 'S' = suspendido)
    # Estructura evento: [0]minuto, [1]tipo, [2]dorsal, [3]equipo_abrev
    # ranking: lista de filas con formato -> [0] nombre | [1] equipo | [2] goles
    ranking = []
    for jugador in jugadores:
        if jugador[4] == 'H':
            goles = 0
            # Contar goles reales del jugador en todos los eventos registrados
            for evento in eventos_partidos:
                if (evento[1] == "Gol" and 
                    evento[2] == jugador[1] and  # mismo dorsal 
                    evento[3] == jugador[3]):    # mismo equipo
                    goles += 1
            
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

def calcular_estadisticas_arbitros(resultados, arbitros, eventos_partidos):
    """Calcula estadísticas de árbitros basadas en eventos reales."""
    stats = []
    
    for arbitro in arbitros:
        if arbitro[2] == 'A':  
            # Contar partidos dirigidos por este árbitro
            partidos_dirigidos = 0
            tarjetas_mostradas = 0
            
            arbitros_activos = 0
            for arb in arbitros:
                if arb[2] == 'A':
                    arbitros_activos += 1
            
            # Contar todas las tarjetas de todos los partidos
            total_tarjetas = 0
            for evento in eventos_partidos:
                if evento[1] in ("Tarjeta Amarilla", "Tarjeta Roja"):
                    total_tarjetas += 1
            

            if arbitros_activos > 0:
                tarjetas_mostradas = total_tarjetas / arbitros_activos
                #max es para que si el resultado es 0, se asigne 1
                partidos_dirigidos = max(1, len(eventos_partidos) / arbitros_activos)
            else:
                tarjetas_mostradas = 0
                partidos_dirigidos = 0
            
            if partidos_dirigidos > 0:
                promedio = tarjetas_mostradas / partidos_dirigidos
            else:
                promedio = 0
                
            stats.append([arbitro[0], partidos_dirigidos, tarjetas_mostradas, promedio])
    
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
