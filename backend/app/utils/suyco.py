# base_datos = {
#     "empleados": {
#         "columnas": {
#             "id": {"tipo": "entero", "restricciones": ["CLAVE PRIMARIA", "AUTOINCREMENTAL"]},
#             "nombre": {"tipo": "texto", "restricciones": ["NO NULO"]},
#             "edad": {"tipo": "entero", "restricciones": ["NO NULO"]},
#             "departamento_id": {"tipo": "entero", "restricciones": ["CLAVE FORANEA", "NO NULO"]}
#         },
#         "llave_primaria": "id",
#         "llaves_foraneas": {"departamento_id": "departamentos.id"}
#     },
#     "departamentos": {
#         "columnas": {
#             "id": {"tipo": "entero", "restricciones": ["CLAVE PRIMARIA", "AUTOINCREMENTAL"]},
#             "nombre": {"tipo": "texto", "restricciones": ["NO NULO"]}
#         },
#         "llave_primaria": "id"
#     }
# }

# def obtener_columnas(tabla):
#     if tabla in base_datos:
#         return list(base_datos[tabla]["columnas"].keys())
#     else:
#         return f"La tabla '{tabla}' no existe en la base de datos."
# columnas_disponibles = list(base_datos["empleados"]["columnas"].keys())

# # Ejemplo: Obtener las columnas de la tabla "empleados"
# columnas_empleados = obtener_columnas("empleados")
# print(columnas_empleados)
# print(columnas_disponibles)

# gaa= ['id', 'nombre', 'edad', 'departamento_id']
# for g in gaa:
#     print(g)