from collections import defaultdict
from icecream import ic


def create_graph(point_pairs):
    graph = defaultdict(list)
    for n1, n2 in point_pairs:
        graph[n1].append(n2)
        graph[n2].append(n1)

    return graph


def is_in_cycle(start_node, graph):
    unvisited = [start_node]
    visited = set()
    previous_added = None

    while unvisited:
        p = unvisited.pop(0)

        if previous_added and p == start_node: return True

        if p in visited: continue

        unvisited = [e for e in graph[p] if e != previous_added] + unvisited
        visited.add(p)
        previous_added = p

    return False


p1 = (1, 2)
p2 = (2, 3)
p3 = (3, 4)
p4 = (2, 4)
p5 = (5, 3)

created_graph = create_graph([p1, p2, p3, p4, p5])

expected = {
    1: [2],
    2: [1, 4, 3],
    3: [2, 4, 5],
    4: [2, 3],
    5: [3]
}

assert len(created_graph) == len(expected)

for k in expected:
    assert sorted(expected[k]) == sorted(created_graph[k])


assert not is_in_cycle(1, created_graph)
assert is_in_cycle(2, created_graph)
assert is_in_cycle(3, created_graph)
assert is_in_cycle(4, created_graph)
assert not is_in_cycle(5, created_graph)
