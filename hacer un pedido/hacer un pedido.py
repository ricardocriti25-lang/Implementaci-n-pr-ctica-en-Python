# Arbol de datos
arbol = {50: (30, 70), 30: (20, 40), 70: (60, 80)}

# 1. Recorrido Preorden
def Preorden(nodo):
    if nodo is not None:
        izquierdo, derecho = arbol.get(nodo, (None, None))
        print(nodo, end=" ")
        Preorden(izquierdo)
        Preorden(derecho)

# 2. Recorrido Inorden
def Inorden(nodo):
    if nodo is not None:
        izquierdo, derecho = arbol.get(nodo, (None, None))
        Inorden(izquierdo)
        print(nodo, end=" ")
        Inorden(derecho)

# 3. Recorrido Postorden
def Postorden(nodo):
    if nodo is not None:
        izquierdo, derecho = arbol.get(nodo, (None, None))
        Postorden(izquierdo)
        Postorden(derecho)
        print(nodo, end=" ")

# 4. Recorrido por niveles
def PorNiveles(raiz):
    if raiz is None:
        return
    cola = [raiz]
    while cola:
        nodo = cola.pop(0)
        print(nodo, end=" ")
        izquierdo, derecho = arbol.get(nodo, (None, None))
        if izquierdo is not None:
            cola.append(izquierdo)
        if derecho is not None:
            cola.append(derecho)

# 5. Buscar un numero
def Buscar(nodo, valor):
    if nodo is None:
        return False
    if nodo == valor:
        return True
    izquierdo, derecho = arbol.get(nodo, (None, None))
    if valor < nodo:
        return Buscar(izquierdo, valor)
    else:
        return Buscar(derecho, valor)

# 6. Eliminar el nodo 20
def Eliminar20():
    arbol[30] = (None, 40)

# Mostrar los resultados
print("Preorden:")
Preorden(50)

print("\nInorden:")
Inorden(50)

print("\nPostorden:")
Postorden(50)

print("\nRecorrido por niveles:")
PorNiveles(50)

print("\nBuscar 60:", Buscar(50, 60))
print("Buscar 90:", Buscar(50, 90))

Eliminar20()
print("Inorden despues de eliminar 20:")
Inorden(50)