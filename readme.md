# Instalacion

## Crear el entorno

```bash
python -m venv env
```

## Activar el entorno

```bash
./env/Scripts/activate
```

## Instalar librerias

```bash
pip install -r requirements.txt
```

## Ejecutar

```bash
python main.py
```

## Modelo

### Producto
- **_id**: ObjectId - Identificador único del producto.
- **codigo**: String - Código del producto.
- **referencia**: String - Referencia del producto.
- **marca**: String - Marca del producto.
- **genero**: String - Género al que está dirigido el producto (por ejemplo, masculino, femenino, unisex).
- **estado**: String - Estado actual del producto (por ejemplo, nuevo, usado).
- **linea**: String - Línea de productos a la que pertenece.
- **color**: String - Color del producto.
- **talla**: String - Talla del producto.
- **grupo**: String - Grupo al que pertenece el producto.
- **ult_compra**: String - Fecha de la última compra.
- **inventario_tienda**: Array[InventarioTienda] - Inventario del producto en diferentes tiendas.
- **devolucion_proveedor**: Object - Información sobre devoluciones al proveedor.
- **garantias**: Object - Información sobre garantías del producto.
- **averias_donaciones**: Object - Información sobre averías y donaciones.
- **nonos_trocados**: Object - Información sobre productos no conformes intercambiados.
- **mercancia_consignacion**: Object - Información sobre mercancía en consignación.
- **ventas_institucionales**: Object - Información sobre ventas a instituciones.
- **total**: Number - Cantidad total disponible del producto.

### InventarioTienda
- **id**: Number - Identificador único del inventario en la tienda.
- **bodega**: String - Nombre o código de la bodega.
- **inventario**: Number - Cantidad de inventario disponible en la tienda.
- **producto_id**: ObjectId - Referencia al producto (relación con `Producto`).