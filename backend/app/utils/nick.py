# from AnalizadorLexico import analizar_lexico
# from AnalizadorSintactico import analizar_sintaxis
# from clases.Eliminar import *
# from clases.Soltar import *
# from clases.Seleccion import *
# from clases.Actualizar import *
# from clases.Alterar import *

# query = """
# INSERTAR EN empleados (nombre, edad, departamento_id) VALORES ("Andre", 30, 1)
# """
# #ALTERAR TABLA empleados AGREGAR casa ENTERO CLAVE PRIMARIA 
# resultado_lexico = analizar_lexico(query)
# print("Resultado del analisis lexico:")
# for token in resultado_lexico:
#     print(token)

# # Base de datos simulada con restricciones y auto-incremental
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

# resultado_sintactico = analizar_sintaxis(query)
# print("\nResultado del analisis sintactico:")
# print(type(resultado_sintactico))
# print(resultado_sintactico.ejecutar(base_datos))

