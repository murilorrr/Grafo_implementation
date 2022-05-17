from grafo import Grafo
import pytest

list_of_nodes = [("A", "B"), ("A", "C"), ("A", "D"), ("B", "D")]
grafo = Grafo(list_of_nodes)


def test_if_grafo_has_a_vertices():
    vertices = grafo.get_vertices()
    assert vertices == ['A', 'B', 'C', 'D']


def test_if_grafo_has_a_arestas():
    expect_return = [('A', 'C'), ('A', 'B'), ('A', 'D'), ('B', 'A'),
                     ('B', 'D'), ('C', 'A'), ('D', 'B'), ('D', 'A')]

    arestas = grafo.get_arestas()
    for node in arestas:
        assert node in expect_return


def test_if_grafo_can_identify_arestas():
    assert grafo.existe_aresta("A", "D") is True
    assert grafo.existe_aresta("A", "E") is False


def test_if_grafo_can_transcript_to_string():
    expect_return = "Grafo: A aponta para ['B', 'C', 'D'] B aponta para ['A', 'D'] C aponta para ['A'] D aponta para ['B', 'A']"
    string_grafo = str(grafo)
    assert string_grafo == expect_return


def test_if_grafo_has_len():
    assert len(grafo) == 4


def test_if_grafo_can_get_arestas_in_one_node():
    get_A = grafo.__getitem__("A")
    assert get_A == {"C", "D", "B"}


def test_error_case():
    list_of_nodes = [("B", "D", "E")]
    with pytest.raises(ValueError):
        grafo = Grafo(list_of_nodes)

print(["A", "B", "C", "D"] == ["A", "B", "D", "C"])