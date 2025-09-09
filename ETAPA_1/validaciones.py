
"""Valida que un valor esté en una lista de opciones permitidas."""
def validar_opcion(valor, opciones_validas, entidad):

    return valor in opciones_validas

"""Verifica que un valor sea único en una lista según un campo específico."""
def validar_unico(lista, valor, campo, entidad):
    i = 0
    while i < len(lista):
        if lista[i][campo] == valor:
            return False
        i = i + 1
    return True

def validar_unico_doble(lista, valor1, campo1, valor2, campo2, entidad):
    i = 0
    while i < len(lista):
        if int(lista[i][campo1]) == valor1 and lista[i][campo2] == valor2:
            return False
        i = i + 1
    return True

"""Verifica que un valor sea único en una lista según un campo específico, excluyendo un índice específico (para actualizaciones)."""
def validar_unico_actualizar(lista, valor, campo, indice_excluir, entidad):
    i = 0
    while i < len(lista):
        if i != indice_excluir and lista[i][campo] == valor:
            return False
        i = i + 1
    return True

"""Valida que una cadena no esté vacía."""
def validar_cadena_no_vacia(texto, entidad):

    return len(texto.strip()) > 0

"""Valida que el dorsal esté entre 1 y 99."""
def validar_dorsal(dorsal):

    return dorsal.isdigit() and 1 <= int(dorsal) <= 99

"""Valida que la posición sea 'ARQ', 'DEF', 'MED' o 'DEL'."""
def validar_posicion(pos):

    return pos in ('ARQ', 'DEF', 'MED', 'DEL')

"""Valida que el estado del partido sea 'Pendiente', 'Finalizado' o 'Suspendido'."""
def validar_estado_partido(estado):

    return estado in ('Pendiente', 'Finalizado', 'Suspendido')

"""Valida que el minuto esté entre 0 y 120."""
def validar_minuto_evento(minuto):

    return 0 <= minuto <= 120

"""Valida que el tipo de evento sea 'Gol', 'Asistencia', 'Tarjeta Amarilla', 'Tarjeta Roja' o 'Expulsión'."""
def validar_tipo_evento(tipo):

    return tipo in ('Gol', 'Asistencia', 'Tarjeta Amarilla', 'Tarjeta Roja', 'Expulsión')

"""Valida que el jugador pertenezca a uno de los equipos del partido y esté habilitado."""
def validar_jugador_en_partido(jugadores, dorsal, equipo, local, visitante):

    for jugador in jugadores:
        if int(jugador[1]) == dorsal and jugador[3] == equipo and jugador[4] == 'H':
            if equipo == local or equipo == visitante:
                return True  # Retorna True si el jugador es válido para el partido
    return False  # Retorna False si el jugador no es válido

"""Valida que los equipos local y visitante sean diferentes."""
def validar_equipos_diferentes(local, visitante):

    return local != visitante

"""Valida que ambos equipos estén habilitados ('H')."""
def validar_equipos_habilitados(equipos, local, visitante):
    local_habilitado = False
    visitante_habilitado = False
    
    for equipo in equipos:
        if equipo[1] == local and equipo[2] == 'H':
            local_habilitado = True
        if equipo[1] == visitante and equipo[2] == 'H':
            visitante_habilitado = True
    
    return local_habilitado and visitante_habilitado

"""Solicita un entero validado dentro de un rango específico."""
def obtener_entero_valido(mensaje, min_val, max_val):
    texto = input(mensaje)
    while not (texto.isdigit() and min_val <= int(texto) <= max_val):
        if not texto.isdigit():
            print("Debe ingresar un número entero válido.")
        else:
            valor_tmp = int(texto)
            if valor_tmp < min_val or valor_tmp > max_val:
                print(f"El valor debe estar entre {min_val} y {max_val}.")
        texto = input(mensaje)
    return int(texto)

"""Solicita una opción válida de una lista de opciones."""
def obtener_opcion_valida(mensaje, opciones_validas):
    valor = input(mensaje)
    while valor not in opciones_validas:
        opciones_str = ""
        i = 0
        while i < len(opciones_validas):
            if i == 0:
                opciones_str = str(opciones_validas[i])
            else:
                opciones_str = opciones_str + ", " + str(opciones_validas[i])
            i += 1
        print(f"Opción inválida. Debe ser una de: {opciones_str}")
        valor = input(mensaje)
    return valor

"""Valida que la abreviatura tenga exactamente 3 caracteres."""
def validar_abreviatura_equipo(abrev):

    return len(abrev) == 3

"""Valida que el código del árbitro sea un entero de 1 a 3 dígitos."""
def validar_codigo_arbitro(codigo):

    return 1 <= codigo <= 999

"""Valida que el nombre no esté vacío y tenga al menos 2 caracteres."""
def validar_nombre_persona(nombre):

    return len(nombre.strip()) >= 2

"""Valida que los goles sean un número no negativo."""
def validar_goles(goles):
    return goles >= 0

"""Valida que las fechas de suspensión sean un número no negativo."""
def validar_fecha_suspension(fechas):

    return fechas >= 0

"""Valida que las tarjetas amarillas sean un número no negativo."""
def validar_tarjetas_amarillas(tarjetas):

    return tarjetas >= 0

"""Valida que el estado del equipo sea 'H' o 'S'."""
def validar_estado_equipo(estado):

    return estado in ('H', 'S')

"""Valida que el estado del jugador sea 'H' o 'S'."""
def validar_estado_jugador(estado):
    return estado in ('H', 'S')

"""Valida que el estado del árbitro sea 'A' o 'I'."""
def validar_estado_arbitro(estado):

    return estado in ('A', 'I')

"""Valida que el tipo de sanción sea válido."""
def validar_tipo_sancion(tipo):
    
    return tipo in ('Amarillas', 'Roja', 'Expulsión', 'Sancionado')

"""Valida que un índice esté dentro del rango de una lista."""
def validar_indice_lista(indice, longitud):

    return 0 <= indice < longitud

"""Valida que el resultado tenga el formato correcto (goles_local-goles_visitante)."""
def validar_resultado_partido(resultado):

    if resultado == "-":
        return True  # Retorna True si no hay resultado (partido pendiente)
    
    partes = resultado.split("-")
    if len(partes) != 2:
        return False  # Retorna False si el formato no es válido
    
    # Verificar que ambas partes sean dígitos antes de convertir
    if partes[0].isdigit() and partes[1].isdigit():
        goles_local = int(partes[0])
        goles_visitante = int(partes[1])
        return goles_local >= 0 and goles_visitante >= 0  # Retorna True si los goles son válidos
    else:
        return False  # Retorna False si los valores no son números

"""Valida que la confirmación sea 'S' o 'N'."""
def validar_confirmacion(confirmacion):
    return confirmacion in ('S', 'N')

"""Valida que un número sea positivo."""
def validar_numero_positivo(numero):
    
    return numero > 0

"""Valida que un número sea no negativo."""
def validar_numero_no_negativo(numero):
    
    return numero >= 0

"""Valida que un entero esté dentro de un rango."""
def validar_rango_entero(valor, min_val, max_val):
    return min_val <= valor <= max_val

"""Valida que una lista no esté vacía."""
def validar_lista_no_vacia(lista, mensaje_error):

    if len(lista) == 0:
        print(mensaje_error)
        return False
    return True

"""Valida que haya suficientes equipos habilitados."""
def validar_equipos_suficientes(equipos, minimo):
    
    equipos_habilitados = 0
    for equipo in equipos:
        if equipo[2] == 'H':
            equipos_habilitados += 1
    
    if equipos_habilitados < minimo:
        print(f"Se necesitan al menos {minimo} equipos habilitados.")
        return False
    return True

"""Valida que un equipo tenga suficientes jugadores habilitados."""
def validar_jugadores_suficientes(jugadores, equipo_abrev, minimo):

    jugadores_habilitados = 0
    for jugador in jugadores:
        if jugador[3] == equipo_abrev and jugador[4] == 'H':
            jugadores_habilitados += 1
    
    if jugadores_habilitados < minimo:
        print(f"El equipo {equipo_abrev} necesita al menos {minimo} jugadores habilitados.")
        return False
    return True

"""Valida que haya suficientes árbitros activos."""
def validar_arbitros_suficientes(arbitros, minimo):
    arbitros_activos = 0
    for arbitro in arbitros:
        if arbitro[2] == 'A':
            arbitros_activos += 1
    
    if arbitros_activos < minimo:
        print(f"Se necesitan al menos {minimo} árbitros activos.")
        return False
    return True
