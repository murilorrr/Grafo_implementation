from grafo import Grafo
import pytest


class TestClass:
    def __init__(self):
        list_of_nodes = [("A", "B"), ("A", "C"), ("A", "D"), ("B", "D")]
        self.grafo = Grafo(list_of_nodes)

    def test_if_grafo_has_a_vertices(self):
        assert self.grafo.get_vertices() is ['A', 'B', 'C', 'D']

    def test_if_grafo_has_a_arestas(self):
        expect_return = [('A', 'C'), ('A', 'B'), ('A', 'D'), ('B', 'A'),
                         ('B', 'D'), ('C', 'A'), ('D', 'B'), ('D', 'A')]
        assert self.grafo.get_arestas() is expect_return

    def test_if_grafo_can_identify_arestas(self):
        assert self.grafo.existe_aresta("A", "D") is True
        assert self.grafo.existe_aresta("A", "E") is False

    def test_if_grafo_can_transcript_to_string(self):
        expect_return = "Grafo: {'A': {'C', 'D', 'B'}, 'B': {'D', 'A'},"
        + "'C': {'A'}, 'D': {'B', 'A'}}"
        assert str(self.grafo) == expect_return

    def test_if_grafo_has_len(self):
        assert len(self.grafo) == 4

    def test_if_grafo_can_get_arestas_in_one_node(self):
        assert self.grafo.__getitem__("A") is {"C", "D", "B"}


class Error_test():
    def __init__(self):
        list_of_nodes = [("B", "D", "E")]
        with pytest.raises(AttributeError):
            self.grafo(list_of_nodes)
