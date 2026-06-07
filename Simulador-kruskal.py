class UnionFind:
    def __init__(self, vertices):
        self.padre = {v: v for v in vertices}

    def encontrar(self, v):
        if self.padre[v] != v:
            self.padre[v] = self.encontrar(self.padre[v])
        return self.padre[v]

    def unir(self, a, b):
        raiz_a = self.encontrar(a)
        raiz_b = self.encontrar(b)

        if raiz_a != raiz_b:
            self.padre[raiz_b] = raiz_a
            return True
        return False


vertices = ['A', 'B', 'C', 'D', 'E', 'F']

aristas = [
    ('A', 'B', 4),
    ('A', 'C', 2),
    ('B', 'C', 1),
    ('B', 'D', 5),
    ('C', 'D', 8),
    ('C', 'E', 10),
    ('D', 'E', 2),
    ('D', 'F', 6),
    ('E', 'F', 3)
]


def kruskal(vertices, aristas, minimo=True):

    uf = UnionFind(vertices)

    if minimo:
        aristas_ordenadas = sorted(aristas, key=lambda x: x[2])
        print("\nÁRBOL DE MÍNIMO COSTE\n")
    else:
        aristas_ordenadas = sorted(aristas, key=lambda x: x[2], reverse=True)
        print("\nÁRBOL DE MÁXIMO COSTE\n")

    arbol = []
    costo_total = 0
    paso = 1

    for origen, destino, peso in aristas_ordenadas:

        print(f"PASO {paso}")
        print(f"Evaluando: {origen} -- {destino} ({peso})")

        if uf.unir(origen, destino):
            arbol.append((origen, destino, peso))
            costo_total += peso

            print("✓ Arista agregada")
            print(f"Costo acumulado: {costo_total}")
        else:
            print("✗ Se descarta (forma ciclo)")

        print("-" * 35)

        paso += 1

    print("\nARISTAS DEL ÁRBOL")

    for origen, destino, peso in arbol:
        print(f"{origen} -- {destino} ({peso})")

    print(f"\nCosto total: {costo_total}")

    return arbol


kruskal(vertices, aristas, minimo=True)

print("\n" + "=" * 50)

kruskal(vertices, aristas, minimo=False)