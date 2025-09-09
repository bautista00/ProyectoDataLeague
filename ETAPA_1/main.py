import random
import gestion
import partidos
import estadisticas
import reportes
import validaciones

def main():
    """Función principal que inicia el sistema de gestión de ligas de fútbol amateur."""
    equipos = []  
    jugadores = []  
    arbitros = []  
    resultados = [] 
    
    opcion = -1
    while opcion != 0:
        reportes.mostrar_menu_principal()
        opcion = int(input("Ingrese una opción: "))
        
        if opcion == 1:
            gestion.gestionar_entidades(equipos, jugadores, arbitros)
        elif opcion == 2:
            partidos.crear_fixture(equipos, resultados)
        elif opcion == 3:
            partidos.actualizar_partidos(resultados, jugadores, equipos)
        elif opcion == 4:
            tabla = estadisticas.calcular_tabla_posiciones(resultados, equipos)
            reportes.mostrar_tabla_posiciones(tabla)
        elif opcion == 5:
            ranking = estadisticas.calcular_ranking_goleadores(resultados, jugadores)
            reportes.mostrar_ranking_goleadores(ranking)
        elif opcion == 6:
            sancionados = estadisticas.calcular_sanciones_vigentes(jugadores)
            reportes.mostrar_sanciones_vigentes(sancionados)
        elif opcion == 7:
            abrev = input("Ingrese abreviatura del equipo: ")
            stats = estadisticas.calcular_estadisticas_equipo(resultados, abrev, equipos)
            reportes.mostrar_estadisticas_equipo(stats)
        elif opcion == 0:
            print("Saliendo del sistema...")
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()
