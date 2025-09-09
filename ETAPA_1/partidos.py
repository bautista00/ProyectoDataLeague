import random
import validaciones

"""Crea la matriz de resultados entre equipos."""
def crear_fixture(equipos, resultados):
    
    equipos_habilitados = []
    for equipo in equipos:
        if equipo[2] == 'H':  # Solo equipos habilitados
            equipos_habilitados.append(equipo)
    
    if len(equipos_habilitados) < 2:
        print("Se necesitan al menos 2 equipos habilitados para crear el fixture.")
    else:
        # Inicializar matriz de resultados
        n_equipos = len(equipos_habilitados)
        resultados.clear()
        
        # Crear matriz cuadrada con resultados vacíos
        for i in range(n_equipos):
            fila = []
            for j in range(n_equipos):
                if i == j:
                    fila.append("-")  # Un equipo no juega contra sí mismo
                else:
                    fila.append("-")  # Resultado vacío hasta que se actualice
            resultados.append(fila)
        
        print(f"Fixture creado para {n_equipos} equipos.")
        print("Matriz de resultados inicializada. Use 'Actualizar Partidos' para ingresar resultados.")

"""Permite actualizar resultados de partidos."""
def actualizar_partidos(resultados, jugadores, equipos, eventos_partidos):
    
    if len(resultados) == 0:
        print("No hay fixture creado. Debe crear el fixture primero.")
    else:
        equipos_habilitados = []
        for equipo in equipos:
            if equipo[2] == 'H':
                equipos_habilitados.append(equipo)
        
        if len(equipos_habilitados) == 0:
            print("No hay equipos habilitados.")
        else:
            opcion = -1
            while opcion != 0:
                print("=" * 50)
                print("ACTUALIZAR PARTIDOS")
                print("=" * 50)
                print("1. Ver matriz de resultados")
                print("2. Actualizar resultado")
                print("3. Registrar eventos de partido")
                print("0. Volver")
                print("=" * 50)
                
                opcion = int(input("Ingrese una opción: "))
            
                if opcion == 1:
                    mostrar_matriz_resultados(resultados, equipos_habilitados)
                elif opcion == 2:
                    actualizar_resultado(resultados, equipos_habilitados)
                elif opcion == 3:
                    registrar_eventos_partido(resultados, jugadores, equipos_habilitados, eventos_partidos)
                elif opcion == 0:
                    print("Volviendo al menú de partidos...")
                else:
                    print("Opción inválida. Intente nuevamente.")
        

"""Muestra la matriz de resultados en formato de tabla."""
def mostrar_matriz_resultados(resultados, equipos):
    if len(resultados) == 0:
        print("No hay resultados para mostrar.")
    else:
        print("=" * 80)
        print("MATRIZ DE RESULTADOS")
        print("=" * 80)
        
        # Encabezado con nombres de equipos
        print(f"{'':<15}", end="")
        for equipo in equipos:
            print(f"{equipo[1]:<8}", end="")
        print()
        
        # Filas de resultados
        for i in range(len(resultados)):
            print(f"{equipos[i][1]:<15}", end="")
            for j in range(len(resultados[i])):
                print(f"{resultados[i][j]:<8}", end="")
            print()
        
        print("=" * 80)

"""Permite actualizar el resultado de un partido específico."""
def actualizar_resultado(resultados, equipos):
    print("=" * 40)
    print("ACTUALIZAR RESULTADO")
    print("=" * 40)
    
    # Mostrar equipos disponibles
    print("Equipos disponibles:")
    for i in range(len(equipos)):
        print(f"{i+1}. {equipos[i][0]} ({equipos[i][1]})")
    
    # Seleccionar equipo local
    local = int(input("Seleccione equipo local (número): ")) - 1
    while local < 0 or local >= len(equipos):
        local = int(input("Número inválido. Seleccione equipo local: ")) - 1
    
    # Seleccionar equipo visitante
    visitante = int(input("Seleccione equipo visitante (número): ")) - 1
    while visitante < 0 or visitante >= len(equipos):
        visitante = int(input("Número inválido. Seleccione equipo visitante: ")) - 1
    
    if local == visitante:
        print("Un equipo no puede jugar contra sí mismo.")
    else:
        # Ingresar resultado
        goles_local = int(input(f"Ingrese goles de {equipos[local][0]}: "))
        while goles_local < 0:
            goles_local = int(input("Los goles no pueden ser negativos: "))
        
        goles_visitante = int(input(f"Ingrese goles de {equipos[visitante][0]}: "))
        while goles_visitante < 0:
            goles_visitante = int(input("Los goles no pueden ser negativos: "))
        
        # Actualizar matriz
        resultado = f"{goles_local}-{goles_visitante}"
        resultados[local][visitante] = resultado
        
        # Actualizar resultado inverso (visitante vs local)
        resultado_inverso = f"{goles_visitante}-{goles_local}"
        resultados[visitante][local] = resultado_inverso
        
        print(f"Resultado actualizado: {equipos[local][0]} {resultado} {equipos[visitante][0]}")

"""Registra eventos de un partido específico."""
def registrar_eventos_partido(resultados, jugadores, equipos, eventos_partidos):
    print("=" * 40)
    print("REGISTRAR EVENTOS DE PARTIDO")
    print("=" * 40)
    
    # Mostrar equipos disponibles
    print("Equipos disponibles:")
    for i in range(len(equipos)):
        print(f"{i+1}. {equipos[i][0]} ({equipos[i][1]})")
    
    # Seleccionar equipos
    local = int(input("Seleccione equipo local (número): ")) - 1
    while local < 0 or local >= len(equipos):
        local = int(input("Número inválido. Seleccione equipo local: ")) - 1
    
    visitante = int(input("Seleccione equipo visitante (número): ")) - 1
    while visitante < 0 or visitante >= len(equipos):
        visitante = int(input("Número inválido. Seleccione equipo visitante: ")) - 1
    
    if local == visitante:
        print("Un equipo no puede jugar contra sí mismo.")
    else:
        local_abrev = equipos[local][1]
        visitante_abrev = equipos[visitante][1]
        
        print(f"Registrando eventos: {equipos[local][0]} vs {equipos[visitante][0]}")
        print("Tipos de eventos: Gol, Asistencia, Tarjeta Amarilla, Tarjeta Roja")
        print("Ingrese minuto -1 para finalizar")
        
        # Lista para almacenar eventos
        eventos = []
        
        minuto = 0
        while minuto != -1:
            minuto = int(input("Ingrese minutos del evento: "))
            
            if minuto != -1:
                while not validaciones.validar_minuto_evento(minuto):
                    minuto = int(input("Minutos inválidos (0-120): "))
                
                tipo = input("Ingrese tipo de evento (Gol/Asistencia/Tarjeta Amarilla/Tarjeta Roja): ")
                while not validaciones.validar_tipo_evento(tipo):
                    tipo = input("Tipo inválido. Ingrese Gol, Asistencia, Tarjeta Amarilla o Tarjeta Roja: ")
                
                # Seleccionar equipo
                print("1. Equipo local")
                print("2. Equipo visitante")
                equipo_opcion = int(input("Seleccione equipo: "))
                
                if equipo_opcion == 1:
                    equipo_abrev = local_abrev
                    equipo_nombre = equipos[local][0]
                elif equipo_opcion == 2:
                    equipo_abrev = visitante_abrev
                    equipo_nombre = equipos[visitante][0]
                else:
                    print("Opción inválida.")
                    equipo_abrev = None
                
                # Mostrar jugadores del equipo seleccionado
                jugadores_equipo = []
                equipo_abrev_valido = False
                if equipo_abrev is not None:
                    equipo_abrev_valido = True
                    for jugador in jugadores:
                        if jugador[3] == equipo_abrev and jugador[4] == 'H':
                            jugadores_equipo.append(jugador)
                
                if equipo_abrev_valido == False or len(jugadores_equipo) == 0:
                    if equipo_abrev_valido:
                        print(f"No hay jugadores habilitados en {equipo_nombre}.")
                    registro_valido = False
                else:
                    registro_valido = True
                
                if registro_valido:
                    print(f"Jugadores de {equipo_nombre}:")
                    for i in range(len(jugadores_equipo)):
                        print(f"{i+1}. {jugadores_equipo[i][0]} (Dorsal {jugadores_equipo[i][1]})")
                    
                    jugador_idx = int(input("Seleccione jugador (número): ")) - 1
                    while jugador_idx < 0 or jugador_idx >= len(jugadores_equipo):
                        jugador_idx = int(input("Número inválido. Seleccione jugador: ")) - 1
                    
                    dorsal = int(jugadores_equipo[jugador_idx][1])
                    
                    # Aplicar sanciones según el tipo de evento
                    aplicar_sanciones(jugadores, tipo, dorsal, equipo_abrev, eventos)
                    
                    # Agregar evento a la lista local
                    eventos.append([str(minuto), tipo, str(dorsal), equipo_abrev])
                    # Agregar evento a la lista global 
                    eventos_partidos.append([str(minuto), tipo, str(dorsal), equipo_abrev])
                
                print(f"Evento registrado: Minuto {minuto}, {tipo}, Dorsal {dorsal}, {equipo_nombre}")
        
        # Mostrar resumen de eventos
        if len(eventos) > 0:
            print("=" * 50)
            print("RESUMEN DE EVENTOS")
            print("=" * 50)
            for evento in eventos:
                tipo_texto = evento[1]
                print(f"Minuto {evento[0]}: {tipo_texto} - Dorsal {evento[2]} ({evento[3]})")
            print("=" * 50)

"""Aplica sanciones automáticas según el tipo de evento.""" 
def aplicar_sanciones(jugadores, tipo, dorsal, equipo_abrev, eventos_partido_actual):

    i = 0
    encontrado = False
    while i < len(jugadores) and not encontrado:
        if int(jugadores[i][1]) == dorsal and jugadores[i][3] == equipo_abrev:
            if tipo == 'Tarjeta Amarilla':  # Tarjeta amarilla
                # Contar tarjetas amarillas en este partido específico
                amarillas_en_partido = 0
                for evento in eventos_partido_actual:
                    if (evento[1] == "Tarjeta Amarilla" and 
                        evento[2] == str(dorsal) and 
                        evento[3] == equipo_abrev):
                        amarillas_en_partido += 1
                
                # Si ya tiene una amarilla en este partido, es expulsión por doble amarilla
                if amarillas_en_partido >= 1:
                    fechas = int(jugadores[i][6]) + 1
                    jugadores[i][6] = str(fechas) 
                    jugadores[i][7] = "Doble Amarilla"
                    print(f"Jugador {jugadores[i][0]} EXPULSADO por doble amarilla en el mismo partido.")
                else:
                    # Primera amarilla del partido
                    tarjetas = int(jugadores[i][5]) + 1  # Incrementar tarjetas amarillas totales
                    jugadores[i][5] = str(tarjetas)
                    if tarjetas >= 3:  # 3 tarjetas amarillas totales = 1 fecha de suspensión
                        fechas = int(jugadores[i][6]) + 1
                        jugadores[i][6] = str(fechas)
                        jugadores[i][7] = "Amarillas"
                        print(f"Jugador {jugadores[i][0]} suspendido por acumulación de tarjetas amarillas.")
            elif tipo == 'Tarjeta Roja':  # Tarjeta roja
                fechas = int(jugadores[i][6]) + 1
                jugadores[i][6] = str(fechas)
                jugadores[i][7] = "Roja"
                print(f"Jugador {jugadores[i][0]} suspendido por tarjeta roja.")
            encontrado = True
        else:
            i = i + 1

"""Obtiene el resultado de un partido específico."""
def obtener_resultado_partido(resultados, local, visitante):
    if local < 0 or local >= len(resultados) or visitante < 0 or visitante >= len(resultados):
        return [0, 0]  # Retorna [0,0] si los índices están fuera de rango
    
    resultado_str = resultados[local][visitante]
    if resultado_str == "-":
        return [0, 0]  # Retorna [0,0] si no hay resultado registrado
    
    partes = resultado_str.split("-")
    if len(partes) == 2:
        a = partes[0]
        b = partes[1]
        if a.isdigit() and b.isdigit():
            goles_local = int(a)
            goles_visitante = int(b)
            return [goles_local, goles_visitante]  # Retorna los goles reales del partido
        else:
            return [0, 0]  # Retorna [0,0] si el formato es inválido
    
    return [0, 0]  # Retorna [0,0] si el formato no es válido
