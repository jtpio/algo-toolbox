import networkx as nx
from graph import Graph

# Define the nodes and then the edges

g = Graph()
g.add_node(0)
g.add_node(1)
g.add_node(2)
g.add_node(3)
g.add_node(4)

g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(4, 1)

# Define the equivalent NetworkX graph to test against

gnx = nx.Graph()

gnx.add_edge(0, 1)
gnx.add_edge(1, 2)
gnx.add_edge(1, 3)
gnx.add_edge(4, 1)

assert g.degree(0) == gnx.degree(0)
assert g.degree(1) == gnx.degree(1)
assert g.degree(4) == gnx.degree(4)

diameter, center = g.diameter_center()
assert (center in nx.center(gnx)) == True

# Use network x to generate a random graph and replicate it as a custom graph.
# Then check it returns the same value for some functions


def verify_graph(nx_graph):
    g_gen = Graph()
    for edge in nx.edges(nx_graph):
        g_gen.add_edge(*edge)

    diameter, center = g_gen.diameter_center()
    assert (center in nx.center(nx_graph)) == True
    assert diameter == nx.diameter(nx_graph)

verify_graph(nx.sedgewick_maze_graph())
verify_graph(nx.karate_club_graph())
