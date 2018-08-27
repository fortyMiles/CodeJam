from collections import defaultdict


def create_graph(point_pairs):
    graph = defaultdict(list)
    for n1, n2 in point_pairs:
        graph[n1].append(n2)
        graph[n2].append(n1)

    return graph


def is_in_cycle(start_node, graph):
    unvisited = [(start_node, None)]
    visited = set()

    while unvisited:
        p, parent = unvisited.pop(0)

        if p == start_node and parent is not None: return True
        elif p in visited: continue

        unvisited = [(e, p) for e in graph[p] if e != parent] + unvisited
        visited.add(p)

    return False


def distance(s_node, t_node, graph):
    visited = set()
    unvisited = [s_node]

    distance_map = defaultdict(lambda: float('inf'))
    distance_map[s_node] = 0

    while unvisited:
        p = unvisited.pop(0)

        if p in visited: continue

        for ex in graph[p]:
            distance_map[ex] = min(distance_map[p]+1, distance_map[ex])
            unvisited += graph[p]

        visited.add(p)

    return distance_map[t_node]


def plant_distance(graph: dict):
    nodes = sorted(graph)
    cycled_nodes = [n for n in nodes if is_in_cycle(n, graph)]

    result = []

    for n in graph:
        if n in cycled_nodes: result.append(0)
        else:
            result.append(min(distance(n, c, graph) for c in cycled_nodes))

    return result


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

assert distance(1, 2, created_graph) == 1
assert distance(1, 5, created_graph) == 3
assert distance(1, 3, created_graph) == 2
assert distance(4, 5, created_graph) == 2

assert plant_distance(created_graph) == [1, 0, 0, 0, 1]


if __name__ == '__main__':
    n = int(input())

    for i in range(n):
        m = int(input())
        connections = []
        for _ in range(m):
            connections.append(tuple([int(num) for num in input().split()]))

        graph = create_graph(connections)

        tude_distances = plant_distance(graph)

        print('Case #{}: {}'.format(i+1, ' '.join(map(str, tude_distances))))

