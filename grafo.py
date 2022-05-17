class Grafo(object):
    """Implementação básica de um grafo."""

    def __init__(self, arestas):
        """Inicializa as estruturas base do grafo."""
        self.grafo = dict()
        self.adiciona_arestas(arestas)

    def get_vertices(self):
        """Retorna a lista de vértices do grafo."""
        return list(self.grafo.keys())

    def get_arestas(self):
        """Retorna a lista de arestas do grafo."""
        return [(k, v) for k in self.grafo.keys() for v in self.grafo[k]]

    def adiciona_arestas(self, arestas: 'list[tuple]'):
        """Adiciona arestas ao grafo."""
        for u, v in arestas:
            self.adiciona_arco(u, v)

    def adiciona_arco(self, u, v):
        """Adiciona uma ligação (arco) entre os nodos 'u' e 'v'."""
        if u not in self.grafo:
            self.grafo[u] = set()
        if v not in self.grafo:
            self.grafo[v] = set()
        self.grafo[u].add(v)
        self.grafo[v].add(u)

    def existe_aresta(self, u, v):
        """Existe uma aresta entre os vértices 'u' e 'v'?"""
        return u in self.grafo and v in self.grafo[u]

    def __len__(self):
        return len(self.grafo)

    def __str__(self):
        string = ""
        for node in self.grafo:
            string += f" {node} aponta para "
            apontadores = []
            for related_node in self.grafo[node]:
                   apontadores.append(related_node)
            string += f"{str(apontadores)}"
        return f"{self.__class__.__name__}:{string}"

    def __getitem__(self, v):
        return self.grafo[v]
