import validaciones


"""
Muestra un menú unificado para gestionar 
equipos, jugadores y árbitros.
"""
def gestionar_entidades(equipos, jugadores, arbitros):

    opcion = -1
    while opcion != 0:
        print("=" * 50)
        print("GESTIÓN DE ENTIDADES")
        print("=" * 50)
        print("1. Gestionar Equipos")
        print("2. Gestionar Jugadores")
        print("3. Gestionar Árbitros")
        print("0. Volver al menú principal")
        print("=" * 50)
        
        opcion = int(input("Ingrese una opción: "))
        
        if opcion == 1:
            gestionar_equipos(equipos, jugadores)
        elif opcion == 2:
            gestionar_jugadores(jugadores, equipos)
        elif opcion == 3:
            gestionar_arbitros(arbitros)
        elif opcion == 0:
            print("Volviendo al menú principal...")
        else:
            print("Opción inválida. Intente nuevamente.")

"""
Gestiona los equipos del sistema.
"""
def gestionar_equipos(equipos, jugadores):
    
    opcion = -1
    while opcion != 0:
        print("=" * 40)
        print("GESTIÓN DE EQUIPOS")
        print("=" * 40)
        print("1. Agregar Equipo")
        print("2. Listar Equipos")
        print("3. Actualizar Equipo")
        print("4. Eliminar Equipo")
        print("0. Volver")
        print("=" * 40)
        
        opcion = int(input("Ingrese una opción: "))
        
        if opcion == 1:
            agregar_equipo(equipos)
        elif opcion == 2:
            listar_equipos(equipos)
        elif opcion == 3:
            actualizar_equipo(equipos)
        elif opcion == 4:
            eliminar_equipo(equipos, jugadores)
        elif opcion == 0:
            print("Volviendo al menú de gestión...")
        else:
            print("Opción inválida. Intente nuevamente.")

"""
Agrega un nuevo equipo a la lista tras validar datos.
"""
def agregar_equipo(equipos):

    print("=" * 30)
    print("AGREGAR EQUIPO")
    print("=" * 30)
    
    nombre = input("Ingrese nombre del equipo: ")
    while not validaciones.validar_cadena_no_vacia(nombre, "nombre") or not validaciones.validar_unico(equipos, nombre, 0, "nombre"):
        if not validaciones.validar_cadena_no_vacia(nombre, "nombre"):
            nombre = input("Nombre no puede estar vacío. Ingrese nombre del equipo: ")
        else:
            nombre = input("Nombre de equipo ya existe. Ingrese otro: ")
    
    abrev = input("Ingrese abreviatura (3 caracteres): ")
    while len(abrev) != 3 or not validaciones.validar_unico(equipos, abrev, 1, "abreviatura"):
        if len(abrev) != 3:
            abrev = input("La abreviatura debe tener 3 caracteres: ")
        else:
            abrev = input("Abreviatura ya existe. Ingrese otra: ")
    
    estado = input("Ingrese estado (H=Habilitado, S=Suspendido): ")
    while not validaciones.validar_opcion(estado, ('H', 'S'), "estado"):
        estado = input("Estado inválido. Ingrese H o S: ")
    
    equipos.append([nombre, abrev, estado])
    print(f"Equipo {nombre} ({abrev}) agregado exitosamente.")


"""
Muestra un listado tabulado de todos los equipos.
"""
def listar_equipos(equipos):
    
    print("=" * 50)
    print("LISTADO DE EQUIPOS")
    print("=" * 50)
    print(f"{'NOMBRE':<20} {'ABREV':<8} {'ESTADO':<10}")
    print("-" * 50)
    
    for equipo in equipos:
        estado_texto = "Habilitado" if equipo[2] == 'H' else "Suspendido"
        print(f"{equipo[0]:<20} {equipo[1]:<8} {estado_texto:<10}")
    
    print("=" * 50)

"""
Modifica el nombre o estado de un equipo existente.

"""
def actualizar_equipo(equipos):
    
    if len(equipos) == 0:
        print("No hay equipos registrados.")
    else:
        print("=" * 30)
        print("ACTUALIZAR EQUIPO")
        print("=" * 30)
        
        abrev = input("Ingrese abreviatura del equipo: ")
        indice = buscar_equipo_por_abreviatura(equipos, abrev)
        
        if indice == -1:
            print("Equipo no encontrado.")
        else:
            print(f"Equipo encontrado: {equipos[indice][0]} ({equipos[indice][1]})")
            print("1. Cambiar nombre")
            print("2. Cambiar estado")
            
            opcion = int(input("Seleccione qué desea cambiar: "))
            
            if opcion == 1:
                nuevo_nombre = input("Ingrese nuevo nombre: ")
                while not validaciones.validar_cadena_no_vacia(nuevo_nombre, "nombre") or not validaciones.validar_unico_actualizar(equipos, nuevo_nombre, 0, indice, "nombre"):
                    if not validaciones.validar_cadena_no_vacia(nuevo_nombre, "nombre"):
                        nuevo_nombre = input("Nombre no puede estar vacío: ")
                    else:
                        nuevo_nombre = input("Nombre de equipo ya existe. Ingrese otro: ")
                equipos[indice][0] = nuevo_nombre
                print("Nombre actualizado exitosamente.")
            elif opcion == 2:
                nuevo_estado = input("Ingrese nuevo estado (H=Habilitado, S=Suspendido): ")
                while not validaciones.validar_opcion(nuevo_estado, ('H', 'S'), "estado"):
                    nuevo_estado = input("Estado inválido. Ingrese H o S: ")
                equipos[indice][2] = nuevo_estado
                print("Estado actualizado exitosamente.")
            else:
                print("Opción inválida.")

"""
Elimina un equipo y sus jugadores asociados.
"""
def eliminar_equipo(equipos, jugadores):

    if len(equipos) == 0:
        print("No hay equipos registrados.")
    else:
        print("=" * 30)
        print("ELIMINAR EQUIPO")
        print("=" * 30)
        
        abrev = input("Ingrese abreviatura del equipo: ")
        indice = buscar_equipo_por_abreviatura(equipos, abrev)
        
        if indice == -1:
            print("Equipo no encontrado.")
        else:
            print(f"Equipo encontrado: {equipos[indice][0]} ({equipos[indice][1]})")
            confirmar = input("¿Está seguro de eliminar este equipo? (S/N): ")
            
            if confirmar == 'S':
                # Eliminar jugadores del equipo
                i = 0
                while i < len(jugadores):
                    if jugadores[i][3] == abrev:
                        jugadores.pop(i)
                    else:
                        i = i + 1
                
                # Eliminar equipo
                equipos.pop(indice)
                print("Equipo eliminado exitosamente.")
            else:
                print("Operación cancelada.")

"""
Gestiona los jugadores del sistema.
"""
def gestionar_jugadores(jugadores, equipos):
    
    opcion = -1
    while opcion != 0:
        print("=" * 40)
        print("GESTIÓN DE JUGADORES")
        print("=" * 40)
        print("1. Agregar Jugador")
        print("2. Listar Jugadores")
        print("3. Actualizar Jugador")
        print("4. Eliminar Jugador")
        print("0. Volver")
        print("=" * 40)
        
        opcion = int(input("Ingrese una opción: "))
        
        if opcion == 1:
            agregar_jugador(jugadores, equipos)
        elif opcion == 2:
            listar_jugadores(jugadores)
        elif opcion == 3:
            actualizar_jugador(jugadores)
        elif opcion == 4:
            eliminar_jugador(jugadores)
        elif opcion == 0:
            print("Volviendo al menú de gestión...")
        else:
            print("Opción inválida. Intente nuevamente.")

"""
Agrega un nuevo jugador a la lista tras validar datos.
"""
def agregar_jugador(jugadores, equipos):

    if len(equipos) == 0:
        print("No hay equipos registrados. Debe agregar equipos primero.")
    else:
        print("=" * 30)
        print("AGREGAR JUGADOR")
        print("=" * 30)
        
        nombreCompleto = input("Ingrese nombre y apellido: ")
        while not validaciones.validar_cadena_no_vacia(nombreCompleto, "nombre"):
            nombreCompleto = input("Nombre no puede estar vacío: ")
        
        dorsal = input("Ingrese dorsal (1-99): ")
        while not validaciones.validar_dorsal(dorsal):
            dorsal = input("Dorsal inválido. Ingrese entre 1 y 99: ")
        
        posicion = input("Ingrese posición (ARQ/DEF/MED/DEL): ")
        while not validaciones.validar_posicion(posicion):
            posicion = input("Posición inválida. Ingrese ARQ, DEF, MED o DEL: ")
        
        print("Equipos disponibles:")
        for i in range(len(equipos)):
            print(f"{i+1}. {equipos[i][0]} ({equipos[i][1]})")
        
        equipo_idx = int(input("Seleccione equipo (número): ")) - 1
        while equipo_idx < 0 or equipo_idx >= len(equipos):
            equipo_idx = int(input("Número inválido. Seleccione equipo: ")) - 1
        
        equipo_abrev = equipos[equipo_idx][1]
        
        # Verificar que el dorsal sea único en el equipo (sin tuplas)
        while not validaciones.validar_unico_doble(jugadores, int(dorsal), 1, equipo_abrev, 3, "dorsal en equipo"):
            dorsal = input("Dorsal ya existe en este equipo. Ingrese otro: ")
            while not validaciones.validar_dorsal(dorsal):
                dorsal = input("Dorsal inválido. Ingrese entre 1 y 99: ")
        
        estado = input("Ingrese estado (H=Habilitado, S=Suspendido): ")
        while not validaciones.validar_opcion(estado, ('H', 'S'), "estado"):
            estado = input("Estado inválido. Ingrese H o S: ")
        
        # Estructura jugador: [0]nombre, [1]dorsal, [2]posicion, [3]equipo, [4]estado, [5]tarjetas_amarillas, [6]fechas_suspension, [7]tipo_sancion
        jugadores.append([nombreCompleto, dorsal, posicion, equipo_abrev, estado, "0", "0", ""])
        print(f"Jugador {nombreCompleto} agregado exitosamente.")

"""
Muestra un listado tabulado de todos los jugadores.

"""
def listar_jugadores(jugadores):
    
    if len(jugadores) == 0:
        print("No hay jugadores registrados.")
    else:
        print("=" * 70)
        print("LISTADO DE JUGADORES")
        print("=" * 70)
        print(f"{'NOMBRE':<20} {'DORSAL':<8} {'POS':<6} {'EQUIPO':<8} {'ESTADO':<10}")
        print("-" * 70)
        
        for jugador in jugadores:
            estado_texto = "Habilitado" if jugador[4] == 'H' else "Suspendido"
            print(f"{jugador[0]:<20} {jugador[1]:<8} {jugador[2]:<6} {jugador[3]:<8} {estado_texto:<10}")
        
        print("=" * 70)


"""
Modifica los datos de un jugador existente.
"""
def actualizar_jugador(jugadores):

    if len(jugadores) == 0:
        print("No hay jugadores registrados.")
    else:
        print("=" * 30)
        print("ACTUALIZAR JUGADOR")
        print("=" * 30)
        
        equipo_abrev = input("Ingrese abreviatura del equipo: ")
        dorsal = input("Ingrese dorsal del jugador: ")
        
        indice = buscar_jugador_por_dorsal_y_equipo(jugadores, dorsal, equipo_abrev)
        
        if indice == -1:
            print("Jugador no encontrado.")
        else:
            print(f"Jugador encontrado: {jugadores[indice][0]}")
            print("1. Cambiar nombre")
            print("2. Cambiar posición")
            print("3. Cambiar estado")
            
            opcion = int(input("Seleccione qué desea cambiar: "))
            
            if opcion == 1:
                nuevo_nombre = input("Ingrese nuevo nombre: ")
                while not validaciones.validar_cadena_no_vacia(nuevo_nombre, "nombre"):
                    nuevo_nombre = input("Nombre no puede estar vacío: ")
                jugadores[indice][0] = nuevo_nombre
                print("Nombre actualizado exitosamente.")
            elif opcion == 2:
                nueva_posicion = input("Ingrese nueva posición (ARQ/DEF/MED/DEL): ")
                while not validaciones.validar_posicion(nueva_posicion):
                    nueva_posicion = input("Posición inválida. Ingrese ARQ, DEF, MED o DEL: ")
                jugadores[indice][2] = nueva_posicion
                print("Posición actualizada exitosamente.")
            elif opcion == 3:
                nuevo_estado = input("Ingrese nuevo estado (H=Habilitado, S=Suspendido): ")
                while not validaciones.validar_opcion(nuevo_estado, ('H', 'S'), "estado"):
                    nuevo_estado = input("Estado inválido. Ingrese H o S: ")
                jugadores[indice][4] = nuevo_estado
                print("Estado actualizado exitosamente.")
            else:
                print("Opción inválida.")

"""
Elimina un jugador por equipo y dorsal.

"""
def eliminar_jugador(jugadores):
    
    if len(jugadores) == 0:
        print("No hay jugadores registrados.")
    else:
        print("=" * 30)
        print("ELIMINAR JUGADOR")
        print("=" * 30)
        
        equipo_abrev = input("Ingrese abreviatura del equipo: ")
        dorsal = input("Ingrese dorsal del jugador: ")
        
        indice = buscar_jugador_por_dorsal_y_equipo(jugadores, dorsal, equipo_abrev)
        
        if indice == -1:
            print("Jugador no encontrado.")
        else:
            print(f"Jugador encontrado: {jugadores[indice][0]}")
            confirmar = input("¿Está seguro de eliminar este jugador? (S/N): ")
            
            if confirmar == 'S':
                jugadores.pop(indice)
                print("Jugador eliminado exitosamente.")
            else:
                print("Operación cancelada.")

"""
Gestiona los árbitros del sistema.
"""
def gestionar_arbitros(arbitros):
    
    opcion = -1
    while opcion != 0:
        print("=" * 40)
        print("GESTIÓN DE ÁRBITROS")
        print("=" * 40)
        print("1. Agregar Árbitro")
        print("2. Listar Árbitros")
        print("3. Actualizar Árbitro")
        print("4. Eliminar Árbitro")
        print("0. Volver")
        print("=" * 40)
        
        opcion = int(input("Ingrese una opción: "))
        
        if opcion == 1:
            agregar_arbitro(arbitros)
        elif opcion == 2:
            listar_arbitros(arbitros)
        elif opcion == 3:
            actualizar_arbitro(arbitros)
        elif opcion == 4:
            eliminar_arbitro(arbitros)
        elif opcion == 0:
            print("Volviendo al menú de gestión...")
        else:
            print("Opción inválida. Intente nuevamente.")

"""
Agrega un nuevo árbitro a la lista tras validar datos.
"""
def agregar_arbitro(arbitros):
    
    print("=" * 30)
    print("AGREGAR ÁRBITRO")
    print("=" * 30)
    
    nombre = input("Ingrese nombre y apellido: ")
    while not validaciones.validar_cadena_no_vacia(nombre, "nombre"):
        nombre = input("Nombre no puede estar vacío: ")
    
    codigo = int(input("Ingrese código del árbitro (1-999): "))
    while not validaciones.validar_codigo_arbitro(codigo) or not validaciones.validar_unico(arbitros, codigo, 1, "código"):
        if not validaciones.validar_codigo_arbitro(codigo):
            codigo = int(input("Código debe ser entre 1 y 999. Ingrese código: "))
        else:
            codigo = int(input("Código ya existe. Ingrese otro: "))
    
    estado = input("Ingrese estado (A=Activo, I=Inactivo): ")
    while not validaciones.validar_opcion(estado, ('A', 'I'), "estado"):
        estado = input("Estado inválido. Ingrese A o I: ")
    
    arbitros.append([nombre, codigo, estado])
    print(f"Árbitro {nombre} agregado exitosamente.")

"""
Muestra un listado tabulado de todos los árbitros.
"""
def listar_arbitros(arbitros):
    
    if len(arbitros) == 0:
        print("No hay árbitros registrados.")
    else:
        print("=" * 50)
        print("LISTADO DE ÁRBITROS")
        print("=" * 50)
        print(f"{'NOMBRE':<25} {'CÓDIGO':<10} {'ESTADO':<10}")
        print("-" * 50)
        
        for arbitro in arbitros:
            estado_texto = "Activo" if arbitro[2] == 'A' else "Inactivo"
            print(f"{arbitro[0]:<25} {arbitro[1]:<10} {estado_texto:<10}")
        
        print("=" * 50)

"""
Modifica el nombre o estado de un árbitro existente.
"""
def actualizar_arbitro(arbitros):
    
    if len(arbitros) == 0:
        print("No hay árbitros registrados.")
    else:
        print("=" * 30)
        print("ACTUALIZAR ÁRBITRO")
        print("=" * 30)
        
        codigo = int(input("Ingrese código del árbitro: "))
        indice = buscar_arbitro_por_codigo(arbitros, codigo)
        
        if indice == -1:
            print("Árbitro no encontrado.")
        else:
            print(f"Árbitro encontrado: {arbitros[indice][0]} ({arbitros[indice][1]})")
            print("1. Cambiar nombre")
            print("2. Cambiar estado")
            
            opcion = int(input("Seleccione qué desea cambiar: "))
            
            if opcion == 1:
                nuevo_nombre = input("Ingrese nuevo nombre: ")
                while not validaciones.validar_cadena_no_vacia(nuevo_nombre, "nombre"):
                    nuevo_nombre = input("Nombre no puede estar vacío: ")
                arbitros[indice][0] = nuevo_nombre
                print("Nombre actualizado exitosamente.")
            elif opcion == 2:
                nuevo_estado = input("Ingrese nuevo estado (A=Activo, I=Inactivo): ")
                while not validaciones.validar_opcion(nuevo_estado, ('A', 'I'), "estado"):
                    nuevo_estado = input("Estado inválido. Ingrese A o I: ")
                arbitros[indice][2] = nuevo_estado
                print("Estado actualizado exitosamente.")
            else:
                print("Opción inválida.")

"""
Elimina un árbitro.
"""
def eliminar_arbitro(arbitros):

    if len(arbitros) == 0:
        print("No hay árbitros registrados.")
    else:
        print("=" * 30)
        print("ELIMINAR ÁRBITRO")
        print("=" * 30)
        
        codigo = int(input("Ingrese código del árbitro: "))
        indice = buscar_arbitro_por_codigo(arbitros, codigo)
        
        if indice == -1:
            print("Árbitro no encontrado.")
        else:
            print(f"Árbitro encontrado: {arbitros[indice][0]} ({arbitros[indice][1]})")
            confirmar = input("¿Está seguro de eliminar este árbitro? (S/N): ")
            
            if confirmar == 'S':
                arbitros.pop(indice)
                print("Árbitro eliminado exitosamente.")
            else:
                print("Operación cancelada.")


"""
Busca un equipo por su abreviatura.
Retorna el índice del equipo o -1 si no se encuentra.
"""
def buscar_equipo_por_abreviatura(equipos, abreviatura):
    
    i = 0
    while i < len(equipos):
        if equipos[i][1] == abreviatura:  # Campo 1 es la abreviatura
            return i  # Retorna el índice del equipo encontrado
        i = i + 1
    return -1  # Retorna -1 si no se encuentra el equipo

"""
Busca un jugador por dorsal y equipo.
Retorna el índice del jugador o -1 si no se encuentra.
"""
def buscar_jugador_por_dorsal_y_equipo(jugadores, dorsal, equipo_abrev):
    
    i = 0
    while i < len(jugadores):
        if jugadores[i][1] == dorsal and jugadores[i][3] == equipo_abrev:  # Campo 1 es dorsal, campo 3 es equipo
            return i  # Retorna el índice del jugador encontrado
        i = i + 1
    return -1  # Retorna -1 si no se encuentra el jugador

"""
Busca un árbitro por su código.
Retorna el índice del árbitro o -1 si no se encuentra.
"""
def buscar_arbitro_por_codigo(arbitros, codigo):
    
    i = 0
    while i < len(arbitros):
        if arbitros[i][1] == codigo:  # Campo 1 es el código
            return i  # Retorna el índice del árbitro encontrado
        i = i + 1
    return -1  # Retorna -1 si no se encuentra el árbitro

"""Retorna una lista de equipos con estado 'H' (habilitado)."""
def obtener_equipos_habilitados(equipos):

    habilitados = []
    for equipo in equipos:
        if equipo[2] == 'H':
            habilitados.append(equipo)
    return habilitados

"""Retorna una lista de jugadores habilitados ('H') de un equipo."""
def obtener_jugadores_habilitados_por_equipo(jugadores, abrev):
    
    habilitados = []
    for jugador in jugadores:
        if jugador[3] == abrev and jugador[4] == 'H':
            habilitados.append(jugador)
    return habilitados

"""Retorna una lista de árbitros con estado 'A' (activo)."""
def obtener_arbitros_activos(arbitros):
    
    activos = []
    for arbitro in arbitros:
        if arbitro[2] == 'A':
            activos.append(arbitro)
    return activos
