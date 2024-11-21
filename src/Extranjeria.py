from collections import Counter, defaultdict, namedtuple
import csv


RegistroExtranjeria = namedtuple('RegistroExtranjeria', 'distrito,seccion,barrio,pais,hombres,mujeres')



def lee_datos_extranjeria(ruta_fichero):
    res = []
    with open(ruta_fichero, encoding='utf-8') as f:
        linea = csv.reader(f, delimiter=",")
        next(linea)
        for distrito, seccion, barrio, pais, hombres, mujeres in linea:
            hombres = int(hombres)
            mujeres = int(mujeres)

            extranjeria = RegistroExtranjeria(distrito.strip(), seccion.strip(), barrio.strip(), pais.strip(), hombres, mujeres)

            res.append(extranjeria)
    return res

""" numero_nacionalidades_distintas(registros): recibe una lista de tuplas de tipo
 RegistroExtranjeria y devuelve el número de nacionalidades
 distintas presentes en los registros de la lista recibida como parámetro. """

def numero_nacionalidades_distintas(registros):
    res = []
    for r in registros:
        if r.pais not in res:
            res.append(r.pais)
    return len(res)

""" secciones_distritos_con_extranjeros_nacionalidades(registros, paises): recibe una lista de tuplas de tipo
 RegistroExtranjeria y un conjunto de cadenas con nombres de países, y devuelve una lista de tuplas (distrito, seccion)
   con los distritos y secciones en los que hay extranjeros del conjunto de paises dado como parámetro.
     La lista de tuplas devuelta estará ordenada por distrito. """

def secciones_distritos_con_extranjeros_nacionalidades(registros, paises):
    res = set()
    for r in registros:
        if r.pais in paises:
            res.add((r.distrito, r.seccion))
    return sorted(res, key=lambda x:x[0])
    
""" total_extranjeros_por_pais(registros): recibe una lista de tuplas de tipo RegistroExtranjeria 
y devuelve un diccionario de tipo {str:int} en el que las claves son los países y los valores
 son el número total de extranjeros (tanto hombres como mujeres) de cada país. """

def total_extranjeros_por_pais(registros):
    res = defaultdict(int)
    for r in registros:
        res[r.pais] += r.hombres + r.mujeres
    #return sorted(res.items(), key=lambda x:x[1], reverse= True)
    return res

""" top_n_extranjeria(registros, n=3): recibe una lista de tuplas de tipo RegistroExtranjeria y
 devuelve una lista de tuplas (pais, numero_extranjeros) con los n países de los que hay más
   población extranjera en los registros pasados como parámetros. """

def top_n_extranjeria(registros, n=3):
    return sorted(total_extranjeros_por_pais(registros).items(), key = lambda x:x[1], reverse = True)[:n]

""" barrio_mas_multicultural(registros): recibe una lista de tuplas de tipo RegistroExtranjeria 
y devuelve el nombre del barrio en el que hay un mayor número de países de procedencia distintos. """

def barrio_mas_multicultural(registros):
    res = defaultdict(set)
    for r in registros:
        res[r.barrio].add(r.pais)
    contado = {barrio: len(paises) for barrio, paises in res.items()}
    return max(contado, key=contado.get)
    
""" barrio_con_mas_extranjeros(registros, tipo=None): recibe una lista de tuplas de tipo RegistroExtranjeria
 y devuelve el nombre del barrio en el que hay un mayor número de extranjeros, bien sea en total 
 (tanto hombres como mujeres) si tipo tiene el valor None, bien sea de hombres si tipo es 'Hombres', 
 o de mujeres si tipo es 'Mujeres'. """

def barrio_con_mas_extranjeros(registros, tipo = None):
    extranjeros_por_barrio = defaultdict(int)
    for r in registros:
        if tipo == None:
            extranjeros_por_barrio[r.barrio] += r.hombres + r.mujeres
        elif tipo == "HOMBRES":
            extranjeros_por_barrio[r.barrio] += r.hombres
        elif tipo == "MUJERES":
            extranjeros_por_barrio[r.barrio] += r.mujeres
    return max(extranjeros_por_barrio, key = extranjeros_por_barrio.get)

""" pais_mas_representado_por_distrito(registros): recibe una lista de tuplas de tipo RegistroExtranjeria
 y devuelve un diccionario de tipo {str:str} en el que las claves son los distritos y los valores
   los países de los que hay más extranjeros residentes en cada distrito. """

def pais_mas_representado_por_distrito(registros):
    registros_por_distrito = defaultdict(list)
    for r in registros:
        registros_por_distrito[r.distrito].append(r)
    return {distrito: aux(registro) for distrito, registro in registros_por_distrito.items()}

def aux(registro):
    res = defaultdict(int)
    for r in registro:
        res[r.pais]+= r.hombres + r.mujeres
    return max(res, key = res.get)


