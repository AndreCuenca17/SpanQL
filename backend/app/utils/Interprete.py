from .nodeVisitor import node_visitor

class Interprenter(node_visitor):
    def __init__(self):
        pass
    def visit_actualizar(self, nodo):
        pass
    def visit_alterar(self, nodo):
        return self.visit(nodo.nombre_tabla) + self.visit(nodo.alteraciones)
    def visit_crear(self, nodo):
        return self.visit(nodo.nombre_tabla) + self.visit(nodo.columnas) + self.visit(nodo.llave_primaria) + self.visit(nodo.llaves_foraneas)
    def visit_eliminar(self, nodo):
        return self.visit(nodo.columna) + self.visit(nodo.tabla) + self.visit(nodo.clausula)
    def visit_seleccion(self, nodo):
        return self.visit(nodo.columnas) + self.visit(nodo.tabla) + self.visit(nodo.condiciones)
    def visit_soltar(self, nodo):
        pass
    
    