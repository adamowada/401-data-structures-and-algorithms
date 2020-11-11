from challenges.breadth_first_graph.breadth_first_graph import Graph


def test_graph_exists():
    test = Graph()
    assert test


def test_breadth_first_print1():
    test = Graph()
    test.add_edge('Pan', 'Are')
    test.add_edge('Are', 'Met')
    test.add_edge('Are', 'Mon')
    test.add_edge('Met', 'Mon')
    test.add_edge('Met', 'Nar')
    test.add_edge('Met', 'Nab')
    test.add_edge('Mon', 'Nab')
    test.add_edge('Nar', 'Nab')
    assert test.breadth_first('Pan') == 'Pan, Are, Met, Mon, Nar, Nab, '


def test_breadth_first_print2():
    test = Graph()
    test.add_edge(0, 1)
    test.add_edge(1, 2)
    test.add_edge(1, 3)
    test.add_edge(1, 4)
    test.add_edge(1, 5)
    test.add_edge(5, 0)
    assert test.breadth_first(3) == '3, 1, 0, 2, 4, 5, '
