def mostrar_menu_principal():
    """Muestra el menú principal del sistema."""
    print("=" * 60)
    print("SISTEMA DE GESTIÓN DE LIGAS DE FÚTBOL")
    print("=" * 60)
    print("1. Gestionar Entidades (Equipos, Jugadores, Árbitros)")
    print("2. Crear Fixture")
    print("3. Actualizar Partidos")
    print("4. Ver Tabla de Posiciones")
    print("5. Ver Ranking de Goleadores")
    print("6. Ver Sanciones Vigentes")
    print("7. Ver Estadísticas de Equipo")
    print("0. Salir")
    print("=" * 60)

def mostrar_tabla_posiciones(tabla):
    """Muestra la tabla de posiciones en formato tabulado."""
    if len(tabla) == 0:
        print("No hay datos para mostrar la tabla de posiciones.")
    else:
        print("=" * 80)
        print("TABLA DE POSICIONES")
        print("=" * 80)
        print(f"{'POS':<4} {'EQUIPO':<8} {'PJ':<4} {'PG':<4} {'PE':<4} {'PP':<4} {'GF':<4} {'GC':<4} {'DG':<4} {'PTS':<4}")
        print("-" * 80)
        
        for i in range(len(tabla)):
            posicion = i + 1
            equipo = tabla[i][0]
            pj = tabla[i][1]
            pg = tabla[i][2]
            pe = tabla[i][3]
            pp = tabla[i][4]
            gf = tabla[i][5]
            gc = tabla[i][6]
            dg = tabla[i][7]
            pts = tabla[i][8]
            
            print(f"{posicion:<4} {equipo:<8} {pj:<4} {pg:<4} {pe:<4} {pp:<4} {gf:<4} {gc:<4} {dg:<4} {pts:<4}")
        
        print("=" * 80)

"""Muestra el ranking de goleadores en formato tabulado."""
def mostrar_ranking_goleadores(ranking):
    if len(ranking) == 0:
        print("No hay datos para mostrar el ranking de goleadores.")
    else:
        print("=" * 60)
        print("RANKING DE GOLEADORES")
        print("=" * 60)
        print(f"{'POS':<4} {'JUGADOR':<25} {'EQUIPO':<8} {'GOLES':<6}")
        print("-" * 60)
        
        for i in range(len(ranking)):
            posicion = i + 1
            jugador = ranking[i][0] #nombre completo
            equipo = ranking[i][1] #abreviatura
            goles = ranking[i][2] #goles
            
            print(f"{posicion:<4} {jugador:<25} {equipo:<8} {goles:<6}")
        
        print("=" * 60)

"""Muestra los jugadores con sanciones vigentes."""
def mostrar_sanciones_vigentes(sancionados):
    if len(sancionados) == 0:
        print("No hay jugadores con sanciones vigentes.")
    else:
        print("=" * 70)
        print("SANCIONES VIGENTES")
        print("=" * 70)
        print(f"{'JUGADOR':<25} {'EQUIPO':<8} {'TIPO':<15} {'FECHAS':<8}")
        print("-" * 70)
        
        for sancionado in sancionados:
            jugador = sancionado[0] #nombre completo
            equipo = sancionado[1] #abreviatura
            tipo = sancionado[2] #tipo de sanción
            fechas = sancionado[3] #fechas
            
            print(f"{jugador:<25} {equipo:<8} {tipo:<15} {fechas:<8}")
        
        print("=" * 70)

"""Muestra las estadísticas de un equipo."""
def mostrar_estadisticas_equipo(estadisticas):
    if len(estadisticas) == 0 or all(x == 0 for x in estadisticas):
        print("No hay estadísticas disponibles para este equipo.")
    else:
        print("=" * 50)
        print("ESTADÍSTICAS DEL EQUIPO")
        print("=" * 50)
        print(f"Partidos Jugados: {estadisticas[0]}") 
        print(f"Partidos Ganados: {estadisticas[1]}")
        print(f"Partidos Empatados: {estadisticas[2]}")
        print(f"Partidos Perdidos: {estadisticas[3]}")
        print(f"Goles a Favor: {estadisticas[4]}")
        print(f"Goles en Contra: {estadisticas[5]}")
        print(f"Diferencia de Goles: {estadisticas[6]}")
        print(f"Puntos: {estadisticas[7]}")
        print("=" * 50)

"""Muestra el historial de partidos de un equipo."""
def mostrar_historial_equipo(historial):
    if len(historial) == 0:
        print("No hay historial disponible para este equipo.")
    else:
        print("=" * 80)
        print("HISTORIAL DE PARTIDOS")
        print("=" * 80)
        print(f"{'FECHA':<6} {'LOCALÍA':<8} {'VS':<8} {'ÁRBITRO':<15} {'ESTADO':<10} {'RESULTADO':<10}")
        print("-" * 80)
        
        for partido in historial:
            fecha = partido[0]
            localia = partido[1]
            vs_equipo = partido[2]
            arbitro = partido[3]
            estado = partido[4]
            resultado = partido[5]
            
            print(f"{fecha:<6} {localia:<8} {vs_equipo:<8} {arbitro:<15} {estado:<10} {resultado:<10}")
        
        print("=" * 80)

"""Muestra las estadísticas de árbitros."""
def mostrar_estadisticas_arbitros(estadisticas):
    if len(estadisticas) == 0:
        print("No hay estadísticas de árbitros disponibles.")
    else:
        print("=" * 70)
        print("ESTADÍSTICAS DE ÁRBITROS")
        print("=" * 70)
        print(f"{'ÁRBITRO':<25} {'PARTIDOS':<10} {'TARJETAS':<10} {'PROMEDIO':<10}")
        print("-" * 70)
        
        for stat in estadisticas:
            arbitro = stat[0]
            partidos = stat[1]
            tarjetas = stat[2]
            promedio = stat[3]
            
            print(f"{arbitro:<25} {partidos:<10} {tarjetas:<10} {promedio:<10.2f}")
        
        print("=" * 70)



