from pymongo import MongoClient

def cargar_lista_diccionarios(lista):
    #Conectar a la base de datos
    cliente = MongoClient('localhost', 27017)
    db = cliente['inventario']
    coleccion = db['inventario_talla']
    #Insertar lista de diccionarios
    coleccion.insert_many(lista)

def formar_array_tiendas(tupla):
    headers = ["CEDI", 	"AD1 JUNIN",	"AD4 ORIENTAL",	"AD3 BELLO",	"AD2 ITAGUI",	"AD5 FLORIDA",	"AD6 LA CENTRAL",	"AS1 SAN NICOLAS",	"AS2 MAYORCA",	"AS3 SANDIEGO",	"AS4 UNICENTRO",	"AS5 MOLINOS",	"AS6 SANTAFE",	"AS7 PUERTA DEL NORTE",	"AS8 PREMIUM PLAZA",	"AS9 ARKADIA",	"MA1 RIONEGRO",	"MA2 MANRIQUE",	"MA3 CALDAS",	"MA4 CASTILLA",	"MA5 SAN JAVIER",	"MA6 GIRARDOTA",	"MA7 SAN ANTONIO DE PRADO",	"MA8 ENVIGADO",	"MA9 BELEN",	"MA10 CARMEN DE VIBORAL",	"MA11 SAN CRISTOBAL",	"MA12 MARINILLA",	"TIENDA VIRTUAL",	"BODEGAS SPORT",	"RESERVA MI AGAVAL","BOD 97","TRANSITO", 	"MEGACENTER"]
    tiendas = []
    for i in headers:
        diccionario = {}
        indice = headers.index(i)
        diccionario["id"] = indice
        diccionario["bodega"] = i
        diccionario["inventario"] = tupla[indice].value
        tiendas.append(diccionario)
    return tiendas