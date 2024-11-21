from Extranjeria import *


def test_lee_datos(registros):
    
    print(f"Se han leido {len(registros)} registros")
    print("Mostrando los 3 primeros:", registros[:3])
    print("mostrando los 3 últimos", registros[-3:])

def test_nacionalidades_distintas(registros):
    print(f"Hay {numero_nacionalidades_distintas(registros)} nacionalidades distintas")

def test_secciones_con_extranjeros(registros, paises):
    print("El resultado es:", secciones_distritos_con_extranjeros_nacionalidades(registros, paises))

def test_total_extranjeros_por_pais(registros):
    print(total_extranjeros_por_pais(registros))

def test_top_n_extranjeria(registros, n = 3):
    print(top_n_extranjeria(registros, n))

def test_barrio_mas_multicultural(registros):
    print(barrio_mas_multicultural(registros))

def test_barrio_con_mas_extranjeros(registros, tipo = None):
    print(barrio_con_mas_extranjeros(registros, tipo))

def test_pais_mas_representado_por_distrito(registros):
    print(pais_mas_representado_por_distrito(registros))

if __name__ == "__main__":
    ruta_fichero = "data/extranjeriaSevilla.csv"
    registros = lee_datos_extranjeria(ruta_fichero)

    test_lee_datos(registros)
    test_nacionalidades_distintas(registros)
    test_secciones_con_extranjeros(registros, paises = {"ALEMANIA", "ITALIA"})
    test_total_extranjeros_por_pais(registros)
    test_top_n_extranjeria(registros)
    test_barrio_mas_multicultural(registros)
    test_barrio_con_mas_extranjeros(registros)
    test_barrio_con_mas_extranjeros(registros, "HOMBRES")
    test_barrio_con_mas_extranjeros(registros, "MUJERES")
    test_pais_mas_representado_por_distrito(registros)