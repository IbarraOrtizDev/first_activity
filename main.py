#Leer el excel INVENTARIO_TALLA.xlsx e imprimir el contenido de la hoja de calculo "hoja 1"
import openpyxl
import helpers

#Cargar el archivo excel
archivo = openpyxl.load_workbook('./INVENTARIO_TALLA.xlsx')
#Obtener la hoja de calculo
hoja = archivo['Hoja1']
listaFilas = list(hoja.iter_rows())

listaObjetosFormateada = []
#Recorrer las filas de la hoja de calculo
for fila in listaFilas[1:len(listaFilas)]:
    objetoCeldas = {
        "codigo": fila[0].value,
        "referencia": fila[1].value,
        "marca": fila[2].value,
        "genero": fila[3].value,
        "estado": fila[4].value,
        "linea": fila[5].value,
        "color": fila[6].value,
        "talla": fila[7].value,
        "grupo": fila[8].value,
        "ult_compra": fila[9].value,
        "inventario_tienda": helpers.formar_array_tiendas(fila[10:44]),
        #"devolucion_proveedor": fila[44].value,
        #"garantias": fila[45].value,
        #"averias_donaciones": fila[46].value,
        #"nonos_trocados": fila[47].value,
        #"mercancia_consignacion": fila[48].value,
        #"ventas_institucionales": fila[50].value,
        "total": fila[51].value
    }
    listaObjetosFormateada.append(objetoCeldas)

helpers.cargar_lista_diccionarios(listaObjetosFormateada)